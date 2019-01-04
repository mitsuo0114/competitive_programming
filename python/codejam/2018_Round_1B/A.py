from unittest import TestCase
from nose.tools import eq_

from decimal import Decimal, ROUND_HALF_UP


def solve(N, L, data):
    min_delta = 100 / N
    remaining = N - sum(data)
    min_fraction = min_delta - int(min_delta)
    if min_fraction < 1.0e-6 :
        return "100"

    fractions = [d * min_fraction - int(d * min_fraction) for d in data]
    fractions = [f if f >= 1.0e-6 else 0 for f in fractions]
    for r in range(0, remaining):
        need_next = True
        for i, f in enumerate(fractions):
            nf = (min_fraction + f) - int(min_fraction + f)
            if f < 0.5 and nf >= 0.5:
                fractions[i] = nf
                data[i] += 1
                need_next = False
                break
        if need_next:
            for i, f in enumerate(fractions):
                nf = (min_fraction + f) - int(min_fraction + f)
                if f < 0.5 and min_fraction < nf:
                    fractions[i] = nf
                    data[i] += 1
                    need_next = False
                    break
        if need_next:
            fractions.append(min_fraction)
            data.append(1)

    return str(sum([Decimal(i * 100.0 / N).quantize(Decimal('0'), rounding=ROUND_HALF_UP) for i in data]))

if __name__=="__main__":
    for case in range(1, int(input()) + 1):
        l = input().split(" ")
        N, L = int(l[0]),int(l[1])
        data = [int(k) for k in input().split(" ")]
        print("Case #%d: %s" % (case, solve(N, L, data)))

class test(TestCase):

    def test_1(self):
        eq_(solve(3, 2, [1, 1]), "100")

    def test_2(self):
        eq_(solve(10, 3, [1, 3, 2]), "100")

    def test_3(self):
        eq_(solve(6, 2, [3, 1]), "101")

    def test_4(self):
        eq_(solve(9, 8, [1,1,1,1,1,1,1,1]), "99")

    def test_5(self):
        eq_(solve(9, 0, []), "100")

    def test_6(self):
        eq_(solve(100, 0, []), "100")

    def test_7(self):
        eq_(solve(10000, 0, []), "200")

    def test_8(self):
        eq_(solve(200, 0, []), "200")
