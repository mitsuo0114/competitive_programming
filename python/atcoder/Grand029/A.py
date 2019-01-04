def solve(N, x, A):
    A = sorted(A)
    count = 0
    for i, a in enumerate(A):
        x -= a
        if i == len(A) - 1:
            if x == 0:
                count += 1
        elif x >= 0:
            count += 1
        else:
            break
    return count

if __name__ == "__main__":
    l = input()
    N, x = int(l.split()[0]),int(l.split()[1])
    A = [int(c) for c in input().split()]
    print(solve(N, x, A))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(3, 70, [20, 30, 10]), 2)

    def test_2(self):
        self.assertEqual(solve(3, 10, [20, 30, 10]), 1)

    def test_3(self):
        self.assertEqual(solve(4, 1111, [1, 10, 100, 1000]), 4)

    def test_4(self):
        self.assertEqual(solve(2, 10, [20, 20]), 0)