def solve(N, M):
    if N > 2 and M > 2:
        return (N - 2) * (M - 2)
    if N == 2 or M == 2:
        return 0
    if N == 1 and M == 1:
        return 1
    return max(max(N, M) - 2, 0)


assert (solve(1, 1) == 1)
assert (solve(1, 2) == 0)
assert (solve(1, 10) == 8)
assert (solve(10, 1) == 8)
assert (solve(2, 1) == 0)
assert (solve(2, 2) == 0)
assert (solve(2, 3) == 0)
assert (solve(2, 4) == 0)
assert (solve(4, 2) == 0)
assert (solve(3, 2) == 0)
assert (solve(3, 3) == 1)
assert (solve(3, 4) == 2)

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    print(solve(N, M))
