def solve(N, M, ABLs):
    ways = {i: [] for i in range(N)}
    for a, b, l in ABLs:
        ways[a - 1].append((b - 1, l))
    visited_way = [[False for _ in range(N)] for _ in range(N)]

    def dfs(i, p, previous_len):
        ans = 0
        for way, current_len in ways[i]:
            if p != -1 and previous_len + current_len == 2540:
                ans += 1
            if not visited_way[way][i]:
                ans += dfs(way, i, current_len)
            visited_way[way][i] = True
        return ans

    ans = 0
    for i in range(N):
        ans += dfs(i, -1, -1)
    return ans


assert (solve(2, 1, [(1, 2, 1000)]) == 0)
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
