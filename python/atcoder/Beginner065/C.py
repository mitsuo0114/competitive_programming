def solve(N, M):
    d = 10 ** 9 + 7
    N, M = min(N, M), max(N, M)
    if abs(N - M) >= 2:
        return 0
    elif abs(N - M) == 1:
        ans = M
    else:
        ans = 2
    for i in range(1, N + 1):
        ans *= pow(i, 2, d)
        ans %= d
    return ans


assert (solve(1, 1) == 2)
assert (solve(2, 2) == 8)
assert (solve(3, 3) == 6 * 6 * 2)
assert (solve(4, 4) == 24 * 24 * 2)

assert (solve(1, 2) == 2)
assert (solve(2, 3) == 6 * 2)
assert (solve(3, 2) == 6 * 2)
assert (solve(1, 8) == 0)
assert (solve(100000, 100000) == 530123477)
if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    print(solve(N, M))

