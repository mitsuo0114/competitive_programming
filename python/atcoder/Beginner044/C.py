import math
from itertools import combinations


def solve(N, A, Xs):
    diffs = [x - A for x in Xs]
    minus = [d for d in diffs if d < 0]
    minuses = {}
    plus = [d for d in diffs if d > 0]
    pluses = {}
    zero = [d for d in diffs if d == 0]

    for n in range(1, len(minus) + 1):
        for ns in combinations(minus, n):
            s = sum(ns)
            minuses.setdefault(s, 0)
            minuses[s] += 1

    for n in range(1, len(plus) + 1):
        for ns in combinations(plus, n):
            s = sum(ns)
            pluses.setdefault(s, 0)
            pluses[s] += 1

    def nCr(n, r):
        f = math.factorial
        return f(n) // f(r) // f(n - r)

    z = sum([nCr(len(zero), r) for r in range(len(zero))])
    c = 0
    for m in minuses:
        c += pluses[-m] * (z + 1)
    c += z
    return c


if __name__ == "__main__":
    N, A = map(int, input().split(" "))
    Xs = map(int, input().split(" "))
    print(solve(N, A, Xs))

# print(solve(4, 8, [7, 9, 8, 9]))
# print(solve(8, 5, [3, 6, 2, 8, 7, 6, 5, 9]))
# print(solve(33, 3, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
