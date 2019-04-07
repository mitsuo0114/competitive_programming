def solve(N, M, ABs):
    ABs = sorted(ABs)
    ans = 0
    for a, b in ABs:
        if b < M:
            ans += a * b
            M -= b
        else:
            ans += M * a
            break
    return ans


if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    ABs = [tuple(map(int, input().split(" "))) for __ in range(N)]
    print(solve(N, M, ABs))
