import math
from itertools import combinations
from collections import Counter


def solve(N, K, Ds):
    while True:
        c = set([int(c) for c in str(N)])
        if len(c.intersection(Ds)) == 0:
            return N
        N += 1


if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    Ds = set(map(int, input().split(" ")))
    print(solve(N, K, Ds))

# print(solve(1000, 8, [1,3,4,5,6,7,8,9]))
# print(solve(8, 5, [3, 6, 2, 8, 7, 6, 5, 9]))
# print(solve(33, 3, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
