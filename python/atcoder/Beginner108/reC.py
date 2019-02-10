def solve(N, K):
    ans = 0
    k = len([n for n in range(1, N + 1) if n % K == 0])
    ans += k * k * k
    if K % 2 == 0:
        k = len([n for n in range(1, N + 1) if n % K == K // 2])
        ans += k * k * k

    return ans


assert (solve(3, 2) == 9)
assert (solve(5, 3) == 1)
assert (solve(31415, 9265) == 27)

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    print(solve(N, K))
