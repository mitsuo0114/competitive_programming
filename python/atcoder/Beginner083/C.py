def solve(X, Y):
    ans = 0
    while X <= Y:
        ans += 1
        X *= 2
    return ans

if __name__ == "__main__":
    X, Y = tuple(map(int, input().split(" ")))
    print(solve(X, Y))
