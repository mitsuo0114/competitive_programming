from unittest import TestCase
from nose.tools import eq_

def solve(N, l):
    ns = [int(n) for n in l.split(" ")]
    actual_sorted = sorted(ns)
    evens = sorted(ns[::2])
    odds = sorted(ns[1::2])

    for i, a in enumerate(actual_sorted):
        if i % 2 == 0:
            if evens[int(i/2)] != a:
                return str(i)
        else:
            if odds[int((i - 1)/2)] != a:
                return str(i)
    return "OK"

for case in range(1, int(input()) + 1):
    N = int(input())
    l = input()
    print("Case #%d: %s" % (case, solve(N, l)))


class test(TestCase):

    def test_1(self):
        eq_(solve(5, "5 6 8 4 3"), "OK")

    def test_2(self):
        eq_(solve(3, "8 9 7"), "1")

    def test_3(self):
        eq_(solve(3, "8 7 9"), "0")

    def test_4(self):
        eq_(solve(3, "9 8 7"), "OK")

    def test_5(self):
        eq_(solve(5, "5 6 8 4"), "0")
        eq_(solve(5, "1 2 3 4"), "OK")
        eq_(solve(5, "3 4 1 2"), "OK")
        eq_(solve(5, "4 4 1 2"), "OK")
        eq_(solve(5, "4 4 2 1"), "0")
