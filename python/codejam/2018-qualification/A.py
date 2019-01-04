from unittest import TestCase
from nose.tools import eq_


def calc(P):
    i = 0
    k = 1
    for p in P:
        if p == "C":
            k *= 2
        elif p == "S":
            i += k
    return i

def solve(l):
    D = int(l.split(" ")[0])
    P = l.split(" ")[1]
    s_count = len([p for p in P if p == "S"])
    if s_count > D:
        return "IMPOSSIBLE"

    hack_count = 0
    while True:
        if calc(P) <= D:
            return str(hack_count)
        else:
            P = P[::-1].replace("SC", "CS", 1)[::-1]
            hack_count += 1

for case in range(1, int(input()) + 1):
    print("Case #%d: %s" % (case, solve(input())))

class test(TestCase):

    def test_d_1(self):
        eq_(calc("S"), 1)
        eq_(calc("S"), 1)
        eq_(calc("S"), 1)
        eq_(calc("SS"), 2)
        eq_(calc("SS"), 2)
        eq_(calc("SS"), 2)
        eq_(calc("CS"), 2)
        eq_(calc("CC"), 0)
        eq_(calc("SCCSSC"), 9)
        eq_(calc("SCCSSC"), 9)
        eq_(calc("SCCSSC"), 9)

    def test_1(self):
        eq_(solve("1 CS"), "1")

    def test_2(self):
        eq_(solve("2 CS"), "0")

    def test_3(self):
        eq_(solve("1 SS"), "IMPOSSIBLE")

    def test_4(self):
        eq_(solve("6 SCCSSC"), "2")
        eq_(solve("6 CSSCS"), "1")

    def test_5(self):
        eq_(solve("2 CC"), "0")

    def test_6(self):
        eq_(solve("3 CSCSS"), "5")

    def test_7(self):
        eq_(solve("1 CCCCS"), "4")

    def test_8(self):
        eq_(solve("1 CCCSC"), "3")

    def test_9(self):
        eq_(solve("2 CCCCCS"), "4")

    def test_10(self):
        eq_(solve("0 "), "0")
        eq_(solve("1 "), "0")

    def test_11(self):
        eq_(solve("0 C"), "0")
        eq_(solve("1 C"), "0")

    def test_12(self):
        eq_(solve("8 CSSCS"), "0")
        eq_(solve("7 CSSCS"), "1")

    def test_13(self):
        eq_(solve("8 CCCS"), "0")
        eq_(solve("8 CCCCS"), "1")
        eq_(solve("8 CCCCCS"), "2")
