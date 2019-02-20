from collections import Counter


def solve(N, M, ABLs):
    Ls = [Counter() for __ in range(N + 1)]
    for a, b, l in ABLs:
        Ls[a].update([l])
        Ls[b].update([l])

    ans = 0
    for n in range(1, N + 1):
        for l, c in Ls[n].items():
            if l > 1270:
                continue
            if l == 1270:
                ans += c * (c - 1) // 2
            else:
                ans += c * Ls[n][2540 - l]
    return ans


assert (solve(2, 1, [(1, 2, 1000)]) == 0)
assert (solve(4, 3, [(1, 2, 1270), (2, 3, 1270), (3, 4, 1270)]) == 2)
assert (solve(4, 3, [(1, 3, 1270), (2, 3, 1270), (3, 4, 1270)]) == 3)
assert (solve(4, 3, [(1, 2, 1420), (2, 3, 1120), (3, 4, 1420)]) == 2)
assert (solve(4, 2, [(1, 2, 1920), (3, 4, 1125)]) == 0)
assert (solve(4, 2, [(1, 2, 2539), (2, 3, 1), (3, 4, 2539)]) == 2)
assert (solve(5, 2, [(1, 3, 2539), (2, 3, 2539), (3, 4, 1), (3, 5, 1)]) == 4)
assert (solve(5, 2, [(1, 3, 1000), (2, 3, 1000), (3, 4, 1340), (4, 5, 1200)]) == 1)
assert (solve(8, 6, [(1, 2, 2539), (2, 3, 1), (3, 4, 2539), (5, 6, 2539), (6, 7, 1), (7, 8, 2539)]) == 4)
assert (solve(4, 2, [(1, 2, 2540), (2, 3, 1), (3, 4, 2540)]) == 0)
assert (solve(4, 2, [(1, 2, 2541), (2, 3, 1), (3, 4, 2541)]) == 0)

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    ABLs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, M, ABLs))
