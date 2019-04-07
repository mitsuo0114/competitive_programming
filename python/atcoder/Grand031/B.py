def solve(N, Cs):
    dp = [-1 for _ in Cs]
    latest_c = {}
    ans = 1
    d = 10 ** 9 + 7
    for i, c in enumerate(Cs):
        if c not in latest_c:
            latest_c[c] = i
            dp[i] = ans
        else:
            previous_i = latest_c[c]
            if previous_i != i - 1:
                ans += dp[previous_i]
            latest_c[c] = i
            dp[i] = ans
    return ans % d


assert (solve(1, [1]) == 1)
assert (solve(2, [1, 1]) == 1)
assert (solve(3, [1, 1, 1]) == 1)
assert (solve(3, [1, 2, 1]) == 2)
assert (solve(3, [2, 1, 1]) == 1)
assert (solve(4, [2, 1, 2, 1]) == 3)
assert (solve(5, [1, 2, 1, 2, 2]) == 3)
assert (solve(5, [1, 2, 1, 1, 2]) == 3)
assert (solve(5, [1, 1, 1, 1, 2]) == 1)
assert (solve(5, [1, 2, 1, 2, 1]) == 5)
assert (solve(7, [1, 3, 1, 2, 3, 3, 2]) == 5)
assert (solve(6, [1, 3, 1, 2, 3, 2]) == 5)
assert (solve(3, [1, 3, 1]) == 2)
assert (solve(4, [1, 3, 1, 2]) == 2)
assert (solve(5, [1, 3, 1, 2, 1]) == 4)

assert (solve(20000, [1] * 20000) == 1)
assert (solve(20000, [1] * 10000 + [2] * 10000) == 1)
assert (solve(6, [1, 2] * 3) == 8)
# assert (solve(6, [4, 2, 5, 4, 2, 4]) == 5)
# assert (solve(7, [1, 3, 1, 2, 3, 2, 1]) == 5)
# assert (solve(7, [1, 3, 1, 2, 1, 2, 3, 2, 1]) == 5)
# assert (solve(6, [1, 3, 1, 2, 3, 2, 4, 3, 4, 1]) == 5)
# assert (solve(6, [1, 3, 1, 2, 3, 2, 4, 3, 4]) == 5)
print("OK")

if __name__ == "__main__":
    N = int(input())
    Cs = [int(input()) for _ in range(N)]
    print(solve(N, Cs))
