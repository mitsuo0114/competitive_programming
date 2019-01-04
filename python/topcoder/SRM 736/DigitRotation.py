# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class DigitRotation:
    def sumRotations(self, X):
        n = len(X)
        sum = 0
        l = []
        if n < 3:
            return 0
        # 1234
        # 1 / 2 / 3 => 3  1  2  [4]
        # 1 / 2 / 4 => 4  1  [3]  2
        # 1 / 3 / 4 => 4  [2]  1  3
        # 2 / 3 / 4 => [1] 4   2  3

        # 12345
        # 1 / 2 / 3 => 3  1  2  [4] [5]
        # 1 / 2 / 4 => 4  1  [3]  2 [5]
        # 1 / 2 / 5 => 5  1  [3] [4] 2
        # 1 / 3 / 4 => 4  [2]  1  3 [5]
        # 1 / 3 / 5 => 5  [2]  1  [4] 3
        # 2 / 3 / 4 => [1] 4   2  3 [5]
        # 2 / 3 / 5 => [1] 4   2  3 [5]
        # 3 / 4/ 5  => [1] [2]  5  3  4

        for a in range(0, n - 2):
            for b in range(a + 1, n - 1):
                for c in range(b + 1, n):
                    if a == 0 and X[c] == "0":
                        continue
                    nX = [ch for ch in X]
                    nX[b] = X[a]
                    nX[a] = X[c]
                    nX[c] = X[b]
                    l.append("".join(nX))
                    sum += int("".join(nX))
        print(l)
        return sum % 998244353
# 4C3
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

def do_test(X, __expected):
    startTime = time.time()
    instance = DigitRotation()
    exception = None
    try:
        __result = instance.sumRotations(X);
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
    sys.stdout.write("DigitRotation (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("DigitRotation.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            X = f.readline().rstrip()
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(X, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534689123
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()
    DigitRotation.sumRotations(None, "12345")

# }}}
# CUT end
