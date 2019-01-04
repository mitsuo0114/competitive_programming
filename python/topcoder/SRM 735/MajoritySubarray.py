# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


class BIT:
    def __init__(self, A):
        self.tree = [0] * (len(A) + 1)

    def add(self, x, i):
        n = len(self.tree)

        while (i < n):
            self.tree[i] += x
            i = i + (i & (-i))

    def sum(self, i):
        s = 0
        while (i > 0):
            s += self.tree[i]
            i = i - (i & (-i))
        return s


class MajoritySubarray:
    def gen(self, n, seed, m):
        A = []
        base = pow(2, 16)
        base2  = pow(2, 31)
        for i in range(0, n):
            A.append((seed // base) % m)
            seed = (seed * 1103515245 + 12345) % (base2)
        return A

    def getCount(self, n, seed, m):
        A = self.gen(n, seed, m)
        n = len(A)
        ans = 0
        for target in range(0, m):
            bit = BIT(A)
            for i in range(0, n):
                if A[i] == target:
                    bit.add(1, i + 1)
                else:
                    bit.add(0, i + 1)
            for s in range(1, n + 1):
                for t in range(s, n + 2):
                    size = (t - s)
                    count = (bit.sum(t - 1) - bit.sum(s - 1))
                    if count > size / 2 and size > 0:
                        ans += 1

        # BIT = ある区間0-kにおけるtarget出現回数
        # target => 0 ~ m -1
        # 区間 s ~ tにおいてtargetが大多数である
        # => BIT(t) - BIT(s) => t - sの出現回数
        #     t - s => t - sの要素数
        #  if (BIT(t) - BIT(s) > (t - s) / 2 => 多数派存在
        #  else => not count

        return ans

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

def do_test(n, seed, m, __expected):
    startTime = time.time()
    instance = MajoritySubarray()
    exception = None
    try:
        __result = instance.getCount(n, seed, m);
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
    sys.stdout.write("MajoritySubarray (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MajoritySubarray.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            seed = int(f.readline().rstrip())
            m = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, seed, m, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1535119503
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
