def solve(N):
    return int(N / 2) * int((N + 1) / 2)

if __name__ == "__main__":
    l = input()
    N = int(l)
    print(solve(N))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(3), 2)

    def test_2(self):
        self.assertEqual(solve(6), 9)

    def test_3(self):
        self.assertEqual(solve(11), 30)

    def test_4(self):
        self.assertEqual(solve(50), 625)