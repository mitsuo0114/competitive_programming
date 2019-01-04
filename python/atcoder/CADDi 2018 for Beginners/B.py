def solve(N, H, W, ABs):
    ans = 0
    for A, B in ABs:
        ans += min(A // H, B // W)
    return ans


if __name__ == "__main__":
    N, H, W = tuple(map(int, input().split(" ")))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, H, W, ABs))
