def solve(S):
    ans = 0
    tans = 0
    for s in S:
        if s in "ACGT":
            tans += 1
            ans = max(ans, tans)
        else:
            tans = 0
    return ans

if __name__ == "__main__":
    S = input()
    print(solve(S))
