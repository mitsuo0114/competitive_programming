def solve(H, W, candles):
    return ["###", "###", ".##"]

if __name__ == "__main__":
    l = input()
    N, K = int(l.split()[0]),int(l.split()[1])
    candles = [int(c) for c in input().split()]
    print(solve(N, K, candles))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(5, 3, [int(c) for c in "-30 -10 10 20 50".split()]),40)
