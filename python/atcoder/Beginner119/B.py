def solve(N, M, KAs):
    ans = 0
    for m in range(1, M + 1):
        if all(m in KAs[n][1:] for n in range(N)):
            ans += 1
    return ans


if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    KAs = list(list(map(int, input().split(" "))) for _ in range(N))
    print(solve(N, M, KAs))
