def solve(S):
    m = S[0]
    ans = 0
    for c in S:
        if ord(c) <= ord(m):
            ans += 1
            m = c
    return ans


if __name__ == "__main__":
    print(solve(input()))
