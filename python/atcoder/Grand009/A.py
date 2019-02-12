import math


def solve(N, ABs):
    count = 0
    for (a, b) in reversed(ABs):
        k = (a + count)
        n = b * math.ceil(k / b)

        count += n - k
    return count


assert (solve(1, [(2, 3)]) == 1)
assert (solve(2, [(2, 3), (2, 3)]) == 1)
assert (solve(1, [(0, 3)]) == 0)
assert (solve(2, [(0, 1), (0, 2)]) == 0)
assert (solve(2, [(0, 8), (0, 1)]) == 0)
assert (solve(2, [(0, 8), (11, 10)]) == 16)
assert (solve(2, [(0, 8), (17, 10)]) == 8)

assert (solve(2, [(0, 3), (0, 3)]) == 0)
assert (solve(2, [(0, 3), (2, 3)]) == 3)
assert (solve(3, [(3, 5), (2, 7), (9, 4)]) == 7)
assert (solve(7, [(3, 1), (4, 1), (5, 9), (2, 6), (5, 3), (5, 8), (9, 7)]) == 22)

if __name__ == "__main__":
    N = int(input())
    ABs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, ABs))
