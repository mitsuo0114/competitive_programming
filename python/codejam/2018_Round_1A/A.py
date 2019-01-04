from unittest import TestCase
from nose.tools import eq_

def solve2(R, C, H, V, lines):
    vertical_count = [len(l) for c in range(0, C) for l in lines if l[c] == "@" ]
    holizontal_count = [len(c) for l in lines for c in l if c == "@" ]


def solve(R, C, H, V, lines):
    choco_count = len([c for l in lines for c in l if c == "@"])
    piece_count = (H + 1) * (V + 1)
    if choco_count % piece_count != 0:
        return "IMPOSSIBLE"
    one_choco = choco_count / piece_count

    for h in range(1, R):
        for v in range(1, C):
            p1 = len([c for l in lines[:h] for c in l[:v] if c == "@"])
            if p1 > one_choco: break
            if p1 < one_choco: continue

            top_area  = [l[v:] for l in lines[:h]]
            left_area = [l[:v] for l in lines[h:]]
            p2 = len([c for l in lines[:h] for c in l[v:] if c == "@"])
            p3 = len([c for l in lines[h:] for c in l[:v] if c == "@"])
            p4 = len([c for l in lines[h:] for c in l[v:] if c == "@"])

            if (one_choco, one_choco, one_choco, one_choco) == (p1, p2, p3, p4):
                return "POSSIBLE"

    return "IMPOSSIBLE"

if __name__=="__main__":
    for case in range(1, int(input()) + 1):
        l = input().split(" ")
        R, C, H, V = int(l[0]),int(l[1]),int(l[2]),int(l[3])
        lines = []
        for i in range(0, R):
            lines.append(input())
        print("Case #%d: %s" % (case, solve(R, C, H, V, lines)))

class test(TestCase):

    def test_1(self):
        map = [".@@..@",
               ".....@",
               "@.@.@@"]
        eq_(solve(3, 6, 1, 1,map), "POSSIBLE")

    def test_2(self):
        map = ["@@@",
               "@.@",
               "@.@",
               "@@@"]
        eq_(solve(4, 3, 1, 1,map), "IMPOSSIBLE")

    def test_3(self):
        map = [".....",
               ".....",
               ".....",
               "....."]
        eq_(solve(4, 5, 1, 1,map), "POSSIBLE")

    def test_3(self):
        map = ["..@@",
               "..@@",
               "@@..",
               "@@.."]
        eq_(solve(4, 4, 1, 1,map), "IMPOSSIBLE")
