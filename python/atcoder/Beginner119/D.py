Matches = {num: c for num, c in zip([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 5, 5, 4, 5, 6, 3, 7, 6])}


def solve(N, M, As):
    dp = [-1 for _ in range(N + 1)]
    dp[0] = 0
    for i in range(N + 1):
        for a in As:
            c = Matches[a]
            if dp[i] == -1:
                continue
            if i + c <= N:
                dp[i + c] = max(dp[i + c],
                                dp[i] * 10 + a)
    return dp[N]


assert (solve(5, 2, [2, 7]) == 2)
assert (solve(7, 2, [1, 8]) == 8)
assert (solve(7, 2, [1, 3]) == 31)
assert (solve(2, 1, [1]) == 1)
assert (solve(4, 1, [1]) == 11)
assert (solve(10, 1, [1, 8]) == 11111)
assert (solve(5, 1, [1, 7]) == 71)
# print(solve(20, 4, [3, 7, 8, 4]))
assert (solve(20, 4, [3, 7, 8, 4]) == 777773)
assert (solve(101, 9, [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 71111111111111111111111111111111111111111111111111)
# assert (solve(1000, 9, [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 71111111111111111111111111111111111111111111111111)

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    As = list(map(int, input().split(" ")))
    print(solve(N, M, As))
