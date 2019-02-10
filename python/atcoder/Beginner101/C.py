import math


def solve(N, K, As):
    ans = 1
    N = N - K
    return ans + math.ceil(N / (K - 1))


assert (solve(2, 2, [2, 1]) == 1)
assert (solve(2, 2, [1, 2]) == 1)
assert (solve(3, 2, [1, 2, 3]) == 2)
assert (solve(3, 2, [2, 1, 3]) == 2)
assert (solve(3, 2, [2, 3, 1]) == 2)
assert (solve(3, 3, [1, 2, 3]) == 1)
assert (solve(3, 3, [2, 1, 3]) == 1)
assert (solve(3, 3, [2, 3, 1]) == 1)
assert (solve(4, 3, [2, 1, 3, 4]) == 2)
assert (solve(4, 2, [2, 1, 3, 4]) == 3)
assert (solve(5, 3, [3, 2, 1, 3, 4]) == 2)

if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    As = list(map(int, input().split(" ")))
    print(solve(N, K, As))
