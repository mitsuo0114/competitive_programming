def solve(N, XUs):
    p = 380000.0
    ans = 0
    for x, u in XUs:
        if u == "BTC":
            ans += float(x) * p
        else:
            ans += float(x)
    return ans


if __name__ == "__main__":
    N = int(input())
    XUs = list(tuple(input().split(" ")) for _ in range(N))
    print(solve(N, XUs))
