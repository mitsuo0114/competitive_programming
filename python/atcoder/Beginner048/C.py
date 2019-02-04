def solve(N, x, As):
    ans = max(0, As[0] - x)
    As[0] -= ans
    for i in range(0, N - 1):
        d = As[i] + As[i + 1]
        ans += max(0, d - x)
        As[i + 1] -= max(0, d - x)
    return ans


if __name__ == "__main__":
    N, x = map(int, input().split(" "))
    As = list(map(int, input().split(" ")))
    print(solve(N, x, As))
