from math import factorial
def solve(N, K):
    arange = [l for l in range(1, N + 1)]
    brange = [l for l in range(1, N + 1)]
    crange = [l for l in range(1, N + 1)]
    count = 0
    krange = [l for l in range(2, 2 * N + 1) if l % K == 0]
    knrange = { n : [k - n for k in krange if k - n > 0] for n in range(1, N + 1) }
    for a in arange:
        for b in brange:
            for c in crange:
                if b in knrange[a] and c in knrange[b] and a in knrange[c]:
                    count += 1
    return count

if __name__ == "__main__":
    l = input()
    N, K = int(l.split()[0]),int(l.split()[1])
    print(solve(N, K))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(3, 2), 9)

    def test_2(self):
        self.assertEqual(solve(5, 3), 1)

    def test_3(self):
        self.assertEqual(solve(31415, 9265), 27)
    #
    # def test_4(self):
    #     self.assertEqual(solve(35897 , 932), 114191)
    #
