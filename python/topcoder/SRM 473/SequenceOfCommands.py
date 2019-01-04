# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class SequenceOfCommands:

    def result(self, commands):
        cood = [0, 0]
        direction = "UP" ## "RIGHT", "DOWN","LEFT",
        for c in commands:
            if c == "S":
                if direction == "UP":
                    cood[1] += 1
                elif direction == "LEFT":
                    cood[0] -= 1
                elif direction == "DOWN":
                    cood[1] -= 1
                elif direction == "RIGHT":
                    cood[0] += 1

            if c == "L":
                if direction == "UP":
                    direction = "LEFT"
                elif direction == "LEFT":
                    direction = "DOWN"
                elif direction == "DOWN":
                    direction = "RIGHT"
                elif direction == "RIGHT":
                    direction = "UP"

            if c == "R":
                if direction == "UP":
                    direction = "RIGHT"
                elif direction == "LEFT":
                    direction = "UP"
                elif direction == "DOWN":
                    direction = "LEFT"
                elif direction == "RIGHT":
                    direction = "DOWN"
        return cood,direction

    def whatHappens(self, commands):
        joined = "".join(commands)
        run1 = joined
        run2 = joined * 2
        run4 = joined * 4
        if self.result(run1) == ([0, 0], "UP") or \
        self.result(run2) == ([0, 0], "UP") or \
        self.result(run4) == ([0, 0], "UP") :
                return "bounded"
        else:
            return "unbounded"

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(commands, __expected):
    startTime = time.time()
    instance = SequenceOfCommands()
    exception = None
    try:
        __result = instance.whatHappens(commands);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("SequenceOfCommands (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SequenceOfCommands.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            commands = []
            for i in range(0, int(f.readline())):
                commands.append(f.readline().rstrip())
            commands = tuple(commands)
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(commands, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534772700
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
