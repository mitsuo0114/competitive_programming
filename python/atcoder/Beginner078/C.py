def solve(N, M):
    p = 1 / pow(0.5, M)
    return int(((N - M) * 100 + M * 1900) * p)


assert (solve(1, 1) == 1900 * 2)
assert (solve(2, 2) == (2 * 1900) * 4)
assert (solve(10, 2) == 18400)
assert (solve(100, 5) == 608000)

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    print(solve(N, M))
