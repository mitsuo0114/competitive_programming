def solve(N, list):
    d = set()
    for i, l in enumerate(list):
        if l in d:
            return "No"
        if i > 0 and l[0] != list[i - 1][-1]:
            return "No"
        d.add(l)
    return "Yes"


if __name__ == "__main__":
    l = input()
    N = int(l)
    list = [input() for _ in range(0, N)]
    print(solve(N, list))

import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(4, [l.strip() for l in """
hoge
english
hoge
enigma
""".splitlines() if len(l.strip())]), "No")

    def test_2(self):
        self.assertEqual(solve(9, [l.strip() for l in """
        basic
c
cpp
php
python
nadesico
ocaml
lua
assembly
        """.splitlines() if len(l.strip())]), "Yes")

    def test_3(self):
        self.assertEqual(solve(8, [l.strip() for l in """
        a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa
        """.splitlines() if len(l.strip())]), "No")


    def test_4(self):
        self.assertEqual(solve(3, [l.strip() for l in """
abc
arc
agc
        """.splitlines() if len(l.strip())]), "No")
