# -*- coding: utf-8 -*-
import math, string, itertools, fractions, heapq, collections, re, array, bisect

from collections import Counter
class SimpleMathProblem:

    def factor(self, a):
        c = Counter()
        n = a
        i = 2
        while(n > 1 and n != i):
            # print(n, i)
            if n % i == 0:
                c.update([i])
                n //= i
                i = 2
            else:
                i += 1
        if n != 1:
            c.update([n])
        return c
    def bi(self, a, b, n):
        print(f" a = {a}, b = {b}, n = {n}")
        if n == 1:
            return 0
        c = 0
        d = 1
        for bi in bin(b):
            c = 2*c
            d = (d * d) % n
            if bi == "1":
                c += 1
                d = (d * a) % n
        return d

    def mo(self, As, Ns):
        def euc(a, b):
            if b == 0:
                return (a, 1, 0)
            else:
                d, x, y = euc(b, a % b)
                return (d, x, x - (a//b) * y)

        def inv(m, n):
            d, x, y = euc(m, n)
            if x < 0:
                return x + n
            else:
                return x

        N = 1
        for n in Ns:
            N *= n
        Cs = []
        print(f"N = {N}")
        print(f"Ns = {Ns}")
        for n in Ns:
            m = N // n
            print(f"inv({m},{n}) = {inv(m, n)}")
            Cs.append(m * (inv(m, n) % n))
        print(f"Cs = " + str(Cs))
        A = 0
        for a, c in zip(As, Cs):
            A += a * c
        return A % n

    def calculate(self, a, b, c, m):
        print(f"a = {a}, m = {m}")
        if m == 1:
            return 0
        # af = self.factor(a)
        mf = self.factor(m)
        As = []
        print("mf : " + str(mf))
        for p, x in mf.items():
            As.append(pow(a, self.bi(b, c, p - 1)) % p)
        print("As : " + str(As))
        return self.mo(As, mf)

    # def powmod(self, x, n, M):
    #     res = 1
    #     if n > 0:
    #         res = self.powmod(x, n // 2, M)
    #         if n % 2 == 0:
    #             res = (res * res) % M
    #         else:
    #             res = (((res * res) % M) * x) % M
    #     return res
    #
    # def calculate(self, a, b, c, m):
    #     if m > 1:
    #         k = pow(b, c)
    #         return self.powmod(a, k, m)
    #     else:
    #         return 0


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
        return '(%s)' % (','.join((pretty_str(y) for y in x)))
    else:
        return str(x)


def do_test(a, b, c, m, __expected):
    startTime = time.time()
    instance = SimpleMathProblem()
    exception = None
    try:
        __result = instance.calculate(a, b, c, m);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime  # in sec

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
    sys.stdout.write("SimpleMathProblem (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("SimpleMathProblem.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            a = int(f.readline().rstrip())
            b = int(f.readline().rstrip())
            c = int(f.readline().rstrip())
            m = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(a, b, c, m, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1537356130
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T / 60), T % 60))
    sys.stdout.write("Score  : %.2f points\n" % points)


if __name__ == '__main__':
    run_tests()

# }}}
# CUT end

