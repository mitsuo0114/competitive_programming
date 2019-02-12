def solve(N, C, K, Ts):
    Ts.sort()
    count = 0
    ans = 0
    time = 0
    for t in Ts[::-1]:
        if count >= C or t < time - K:
            ans += 1
            count = 0
            time = 0
        count += 1
        if time == 0:
            time = t
    if count > 0:
        ans += 1
    return ans


assert (solve(1, 1, 10, [1]) == 1)
assert (solve(2, 1, 10, [1, 2]) == 2)
assert (solve(2, 2, 10, [1, 2]) == 1)
assert (solve(2, 2, 10, [1, 2, 8]) == 2)
assert (solve(2, 2, 10, [1, 2, 12]) == 2)
assert (solve(4, 2, 10, [2, 2, 2, 12]) == 2)
assert (solve(2, 3, 10, [1, 2]) == 1)
assert (solve(2, 2, 10, [1, 30]) == 2)
assert (solve(2, 2, 10, [1, 1, 30, 30]) == 2)
assert (solve(2, 3, 10, [1, 1, 30, 30]) == 2)
assert (solve(5, 3, 5, [1, 2, 3, 6, 12]) == 3)
assert (solve(6, 3, 3, [7, 6, 2, 8, 10, 6]) == 3)

if __name__ == "__main__":
    N, C, K = tuple(map(int, input().split(" ")))
    Ts = [int(input()) for _ in range(N)]
    print(solve(N, C, K, Ts))
