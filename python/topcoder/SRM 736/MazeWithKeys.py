# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
import copy
from heapq import heappop, heappush

class MazeWithKeys:
    
    def getKeyandGoal(self, currentmap, x, y):
        heapdata = [(x, y)]
        Y = len(currentmap)
        X = len(currentmap[0])
        findings = set()
        visited = set()

        while (len(heapdata) > 0):
            coord = heapdata.pop()

            nx = coord[0]
            ny = coord[1]
            visited.add( coord )
            for (cx, cy) in [(nx + 1, ny), (nx - 1, ny),
                             (nx, ny + 1), (nx, ny - 1)]:
                if cx < 0 or cy < 0 or cx >= X or cy >= Y: continue


                cell = currentmap[cy][cx]
                # print(f"checking next {(cx, cy, cell)}")
                if cell == "#": continue

                if cell == "." and (cx, cy) not in visited:
                    heapdata.append((cx, cy))
                elif cell == "*":
                    findings.add(cell)
                elif "a" <= cell <= "z" and (cx, cy) not in visited:
                    findings.add(cell)
                    heapdata.append((cx, cy))
        return findings

    def startingPoints(self, a):
        okpoint = set()
        Y = len(a)
        X = len(a[0])

        for y in range(0, Y):
            for x in range(0, X):
                if a[y][x] != ".": continue
                currentmap = list(copy.deepcopy(a))
                # print(f"checking {(x, y)}")
                for try_count in range(0, 100): # must be stopped within this count
                    findings = self.getKeyandGoal(currentmap, x, y)
                    # print(findings)

                    if "*" in findings and try_count == 0:
                        # too easy
                        break
                    elif "*" in findings and try_count > 0:
                        okpoint.add((x, y))
                        break
                    elif len(findings) == 0:
                        # could not solve from this coordinate
                        break

                    deletedDoorsandKeys = set()
                    for e in findings:
                        if e != "*": # key
                            deletedDoorsandKeys.add(e)
                            deletedDoorsandKeys.add(e.upper())
                    for c in range(0, Y):
                        for k in list(deletedDoorsandKeys):
                            currentmap[c] = currentmap[c].replace(k, ".")

        return len(okpoint)

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

def do_test(a, __expected):
    startTime = time.time()
    instance = MazeWithKeys()
    exception = None
    try:
        __result = instance.startingPoints(a);
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
    sys.stdout.write("MazeWithKeys (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MazeWithKeys.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            a = []
            for i in range(0, int(f.readline())):
                a.append(f.readline().rstrip())
            a = tuple(a)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(a, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1534944840
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
