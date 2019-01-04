from collections import Counter


def solve(V):
    n = len(V)
    odd_max = Counter(V[1::2]).most_common(2)
    even_max = Counter(V[::2]).most_common(2)

    if odd_max[0][0] != even_max[0][0]:
        return n - odd_max[0][1] - even_max[0][1]
    elif len(odd_max) == 1 and len(even_max) == 1:
        return n // 2
    elif len(odd_max) != 1 and len(even_max) == 1:
        return n - odd_max[1][1] - even_max[0][1]
    elif len(odd_max) == 1 and len(even_max) != 1:
        return n - odd_max[0][1] - even_max[1][1]
    else:
        return n - max(even_max[0][1] + odd_max[1][1],
                       even_max[1][1] + odd_max[0][1])


if __name__ == "__main__":
    n = int(input())
    l = input()
    print(solve(l.split(" ")))

import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(["3", "1", "3", "2"]), 1)

    def test_2(self):
        self.assertEqual(solve(["105", "119", "105", "119", "105", "119"]), 0)

    def test_3(self):
        self.assertEqual(solve(["1", "1", "1", "1"]), 2)

    def test_4(self):
        self.assertEqual(solve(["1", "1", "1", "1", "1", "2", "1", "2"]), 2)

    def test_5(self):
        self.assertEqual(solve(["1", "1", "1", "1", "1", "1", "1", "1"]), 4)

    def test_7(self):
        self.assertEqual(solve(["1", "1", "1", "2", "1", "2", "1", "2"]), 1)

    def test_8(self):
        self.assertEqual(solve(["2", "1", "2", "2", "1", "2", "1", "2"]), 3)

    def test_6(self):
        self.assertEqual(solve(["1", "1", "1", "1", "1", "1", "1", "1"]), 4)
        self.assertEqual(solve(["1", "1", "1", "1", "1", "1", "1", "2"]), 3)
        self.assertEqual(solve(["1", "1", "1", "1", "1", "1", "2", "1"]), 3)
        self.assertEqual(solve(["1", "1", "1", "1", "1", "2", "1", "2"]), 2)
        self.assertEqual(solve(["1", "1", "1", "1", "2", "1", "2", "1"]), 2)
        self.assertEqual(solve(["1", "1", "1", "2", "1", "2", "1", "2"]), 1)
        self.assertEqual(solve(["1", "1", "2", "1", "2", "1", "2", "1"]), 1)
        self.assertEqual(solve(["1", "2", "1", "2", "1", "2", "1", "2"]), 0)
        self.assertEqual(solve(["2", "1", "2", "1", "2", "1", "2", "1"]), 0)

        self.assertEqual(solve(["1", "2", "1", "2", "1", "2", "1", "1"]), 1)
        self.assertEqual(solve(["2", "1", "2", "1", "2", "1", "1", "1"]), 1)
        self.assertEqual(solve(["1", "2", "1", "2", "1", "2", "1", "1"]), 1)
        self.assertEqual(solve(["2", "1", "2", "1", "2", "1", "1", "1"]), 1)

    def test_9(self):
        self.assertEqual(solve(["1", "1", "1", "2", "1", "3", "1"]), 2)

    def test_10(self):
        self.assertEqual(solve(["1", "3", "1", "2", "1", "3", "1"]), 1)
