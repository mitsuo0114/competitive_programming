def lcm(a, b):
    return a if not b else lcm(b, a % b)


assert (lcm(7, 3) == 1)
assert (lcm(6, 3) == 3)
assert (lcm(7, 14) == 7)


def solve(N, M):
    return M - lcm(N, M)


assert (solve(1, 1) == 0)
assert (solve(1, 2) == 1)
assert (solve(3, 2) == 1)
assert (solve(3, 5) == 4)
assert (solve(8, 5) == 4)
assert (solve(10, 5) == 0)
assert (solve(10, 10) == 0)
assert (solve(10, 15) == 10)

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    print(solve(N, M))
