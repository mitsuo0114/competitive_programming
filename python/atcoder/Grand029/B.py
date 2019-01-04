def solve2(N, X, D):
    gtaken = [0 for _ in range(0, N)]
    mincosts = [() for _ in range(0, N)]
    for i in range(N - 1, -1, -1):
        mindata = (5 * D[i] + X, 1)
        for j in range(i, N - 1):
            d, k =  mindata[j]
            if (4 * k + 4) * D[i] + X < d:



        mincosts[i] = mindata


    return sum(mincosts)

def solve(N, X, D):
    gtaken = [0 for _ in range(0, N)]
    takecount = 0
    cost = 0
    owncount = 0
    previous_x = 0
    while takecount < N:
        for i in range(N - 1, -1, -1):
            if gtaken[i] == 1:
                continue
            x = D[i]
            if owncount == 0 or owncount == 1:
                cost += X  # take cost
                cost += abs(x - previous_x) * pow(owncount + 1, 2)  # move cost
                owncount += 1
                gtaken[i] = 1
                takecount += 1
                previous_x = x
            else:
                if X / 2 / (owncount - 1) > x:
                    cost += X  # take cost
                    cost += abs(x - previous_x) * pow(owncount + 1, 2)  # move cost
                    owncount += 1
                    gtaken[i] = 1
                    takecount += 1
                    previous_x = x

        # lift off
        cost += X
        cost += abs(previous_x) * pow(owncount + 1, 2)  # move cost
        owncount = 0

    return cost


if __name__ == "__main__":
    l = input()
    N, x = int(l.split()[0]), int(l.split()[1])
    A = [int(c) for c in input().split()]
    print(solve(N, x, A))

import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(2, 100, [1, 10]), 355)

    def test_2(self):
        self.assertEqual(solve(5, 1, [1, 999999997, 999999998, 999999999, 1000000000]), 19999999983)

    def test_3(self):
        self.assertEqual(solve(10, 8851025, [38, 87, 668, 3175, 22601, 65499, 90236, 790604, 4290609, 4894746]),
                         150710136)

    def test_4(self):
        self.assertEqual(solve(16, 10,
                               [1, 7, 12, 27, 52, 75, 731, 13856, 395504, 534840, 1276551, 2356789, 9384806, 19108104,
                                82684732, 535447408]), 3256017715)
