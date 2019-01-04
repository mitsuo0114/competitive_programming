# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
# import Queue as queue
import heapq

class TheFlippingGame2:
    def search(self, M, startpoint, n, m, c_min):
        destMap = [ [ n*m for _ in range(0, m)] for __ in range(0, n)]

        x, y = startpoint
        pq = []
        destMap[y][x] = 0
        heapq.heappush(pq, (0, x, y))
        maxd = 0
        queued = set()
        while len(pq):
            d, x, y = heapq.heappop(pq)
            queued.add((x,y))

            for (xi, yi) in [(x + 1, y), (x - 1, y),
                             (x, y + 1), (x, y - 1)]:
                if 0 <= xi < m and \
                   0 <= yi < n and \
                  (xi, yi) not in queued:
                    nd = 0 if M[y][x] == M[yi][xi] else 1
                    if (nd + d) < destMap[yi][xi]:
                        destMap[yi][xi] = nd + d
                        maxd = max(maxd, nd + d)
                        if nd + d > c_min:
                            continue
                        heapq.heappush(pq, (nd + d, xi, yi))
                        queued.add((xi, yi))
        return maxd

    def MinimumMoves(self, n, m, M):
        min_dist = n * m
        for rep in ["w", "b"]:
            newM = [ [M[y][x].replace("e", rep) for x in range(0, m)] for y in range(0, n) ]
            for y in range(n):
                for x in range(m):
                    startpoint = (x, y)
                    min_dist = min(min_dist, self.search(newM, startpoint,n , m, min_dist))
        return min_dist + 1

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

def do_test(n, m, x, __expected):
    startTime = time.time()
    instance = TheFlippingGame2()
    exception = None
    try:
        __result = instance.MinimumMoves(n, m, x);
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
    sys.stdout.write("TheFlippingGame2 (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TheFlippingGame2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            m = int(f.readline().rstrip())
            x = []
            for i in range(0, int(f.readline())):
                x.append(f.readline().rstrip())
            x = tuple(x)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, m, x, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1535374696
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
