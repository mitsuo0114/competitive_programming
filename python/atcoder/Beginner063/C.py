from collections import Counter
import string


def solve(N, Ss):
    Ss = sorted(Ss)
    if all([s % 10 == 0 for s in Ss]):
        return 0
    allsum = sum(Ss)
    if allsum % 10 != 0:
        return allsum
    for c in Ss:
        if (allsum - c) % 10 != 0:
            return allsum - c
    return 0


assert (solve(1, [1]) == 1)
assert (solve(1, [2]) == 2)
assert (solve(2, [2, 6]) == 8)
assert (solve(3, [2, 6, 10]) == 18)
assert (solve(3, [2, 4, 6]) == 12)
assert (solve(3, [2, 4, 8]) == 14)
assert (solve(3, [4, 6, 8]) == 18)
assert (solve(3, [10, 10, 10]) == 0)
assert (solve(3, [9, 10, 11, 40]) == 61)
assert (solve(3, [10, 11, 19, 40]) == 69)
assert (solve(3, [5, 10, 15]) == 25)
assert (solve(3, [10, 10, 15]) == 35)
assert (solve(3, [10, 20, 30]) == 0)

if __name__ == "__main__":
    N = int(input())
    Ss = [int(input()) for _ in range(N)]
    print(solve(N, Ss))
