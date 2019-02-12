def solve(Q, H, S, D, N):
    return min(
        N * Q * 4,
        N * H * 2,
        N * S,
        (N // 2) * D + min(S * (N % 2), H * 2 * (N % 2), Q * 4 * (N % 2))
    )


assert (solve(1, 100, 100, 100, 4) == 16)
assert (solve(100, 1, 100, 100, 4) == 8)
assert (solve(100, 100, 1, 100, 4) == 4)
assert (solve(100, 100, 100, 1, 4) == 2)
assert (solve(100, 100, 100, 1, 5) == 102)
assert (solve(1, 100, 100, 1, 5) == 2 + 4)
assert (solve(100, 1, 100, 1, 5) == 2 + 2)
assert (solve(100, 100, 1, 1, 5) == 2 + 1)

if __name__ == "__main__":
    Q, H, S, D = tuple(map(int, input().split(" ")))
    N = int(input())
    print(solve(Q, H, S, D, N))
