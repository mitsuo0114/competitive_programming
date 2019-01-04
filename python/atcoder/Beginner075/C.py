def solve(N, M, ABs):
    ans = 0
    for i in range(M):
        adjMat = [[0 for _ in range(N)] for _ in range(N)]
        for k, (a, b) in enumerate(ABs):
            if k != i:
                adjMat[a - 1][b - 1] = 1
                adjMat[b - 1][a - 1] = 1

        def dps(a, visited):
            n = [i for i, b in enumerate(adjMat[a]) if b == 1]
            for nn in n:
                if nn not in visited:
                    visited.append(nn)
                    dps(nn, visited)
            return visited

        visited = dps(0, [])
        if len(visited) != N:
            ans += 1
    return ans


if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, M, ABs))
