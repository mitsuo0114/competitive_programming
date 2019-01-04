# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
from collections import Counter

class UF:
    def __init__(self, all):
        self.tree = {a : a for a in all}

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b: return
        self.tree[a] = b

    def root(self, a):
        if self.tree[a] == a:
            return a
        else:
            self.tree[a] = self.root(self.tree[a])
            return self.tree[a]

    def samegroup(self, a , b):
        return self.root(a) == self.root(b)


class BuildingSpanningTreesDiv2:



    def getNumberOfSpanningTrees(self, n, x, y):
        union_find = UF([i for i in range(1, n + 1)])

        for i in range(0, n-3):
            if union_find.samegroup(x[i], y[i]): # loop was created
                return 0
            union_find.unite(x[i], y[i])
        counter = Counter([union_find.root(i) for i in range(1, n + 1) ])
        values = list(counter.values())
        return ( (values[0] * values[1] * values[0] * values[2]) +
               (values[1] * values[2] * values[0] * values[1]) +
               (values[1] * values[2] * values[0] * values[2]))  % 987654323

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

def do_test(n, x, y, __expected):
    startTime = time.time()
    instance = BuildingSpanningTreesDiv2()
    exception = None
    try:
        __result = instance.getNumberOfSpanningTrees(n, x, y);
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
    sys.stdout.write("BuildingSpanningTreesDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BuildingSpanningTreesDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            x = []
            for i in range(0, int(f.readline())):
                x.append(int(f.readline().rstrip()))
            x = tuple(x)
            y = []
            for i in range(0, int(f.readline())):
                y.append(int(f.readline().rstrip()))
            y = tuple(y)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, x, y, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1535263679
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
