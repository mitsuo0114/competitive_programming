def solve(N, K, Xs):
    plus = sorted([x for x in Xs if x >= 0])
    minus = sorted([abs(x) for x in Xs if x < 0])
    ans = 10 ** 9
    for i in range(0, K + 1):
        j = K - i
        if i <= len(plus) and i == K:
            p = plus[i-1]
            ans = min(ans, p)
        elif j <= len(minus) and j == K:
            m = minus[j-1]
            ans = min(ans, m)
        elif i <= len(plus) and j <= len(minus):
            p = plus[i - 1]
            m = minus[j - 1]
            ans = min(ans, p * 2 + m, m * 2 + p)

    return ans


assert (solve(4, 2, [2, 1, -1, -2]) == 2)
assert (solve(4, 2, [20, 1, -1, -20]) == 3)
assert (solve(1, 1, [1]) == 1)
assert (solve(1, 1, [0]) == 0)
assert (solve(4, 4, [-1, 0, 1, 2]) == 4)
assert (solve(4, 4, [-1, 0, 1, 200]) == 202)
assert (solve(4, 4, [-100, 0, 1, 2]) == 104)
assert (solve(4, 1, [-100, 0, 101]) == 0)
assert (solve(4, 1, [-1000, 0, 101]) == 0)
assert (solve(4, 2, [-1, 0, 101, 150]) == 1)
assert (solve(4, 3, [-1, 0, 101, 150]) == 103)
assert (solve(4, 4, [-2, -1, 0, 1]) == 4)
assert (solve(4, 4, [-2, -1, 0, 100]) == 104)
assert (solve(3, 3, [0, 1, 2]) == 2)
assert (solve(3, 3, [0, -1, -2]) == 2)
assert (solve(2, 2, [1, 2]) == 2)
assert (solve(3, 2, [-1, 1]) == 3)
assert (solve(8, 5, [-9, -7, -4, -3, 1, 2, 3, 4]) == 10)

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    Xs = list(map(int, input().split(" ")))
    print(solve(N, K, Xs))
