import bisect

def solve(N, ABs, M, Ts):
    ABs = sorted(ABs)
    As = [ab[0] for ab in ABs]

    ans = []
    for t in Ts:
        i = bisect.bisect_right(As, t)
        if i > 0:
            i -= 1
        tans = ABs[i][1] + max(0, (t - ABs[i][0]))
        if i + 1 < N:
            tans = min(tans,ABs[i+1][1] + max(0, (t - ABs[i+1][0])))
        ans.append(tans)
    return "\n".join(str(a) for a in ans)


assert (solve(1, [(2, 10)], 1, [1]) == "10")
assert (solve(1, [(2, 10)], 1, [2]) == "10")
assert (solve(1, [(2, 10)], 2, [2, 3]) == "10\n11")
assert (solve(1, [(2, 10)], 2, [2, 5]) == "10\n13")
assert (solve(2, [(2, 10), (4, 11)], 2, [2, 4]) == "10\n11")
assert (solve(2, [(2, 10), (4, 11)], 2, [2, 5]) == "10\n12")

assert (solve(2, [(5, 6), (3, 5)], 2, [4, 8]) == "6\n9")
assert (solve(4, [(12, 5), (1, 1), (7, 3), (243, 32)], 1, [14]) == "7")
assert (solve(4, [(12, 5), (1, 1), (7, 3), (243, 32)], 6, [632, 188, 69, 54, 14, 36]) == "421\n32\n32\n32\n7\n29")

if __name__ == "__main__":
    N = int(input())
    ABs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    M = int(input())
    Ts = [int(input()) for _ in range(M)]
    print(solve(N, ABs, M, Ts))
