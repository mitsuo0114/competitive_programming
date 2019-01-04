def solve(N, i):
    return N - i + 1

if __name__ == "__main__":
    l = input()
    N, i = int(l.split()[0]),int(l.split()[1])
    print(solve(N,i))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(4, 2), 3)

    def test_2(self):
        self.assertEqual(solve(1, 1), 1)

    def test_3(self):
        self.assertEqual(solve(15, 11), 5)