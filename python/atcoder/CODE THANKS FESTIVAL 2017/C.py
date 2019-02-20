import heapq


def solve(N, K, ABs):
    q = [(a, b) for (a, b) in ABs]
    heapq.heapify(q)

    ans = 0
    for i in range(K):
        a, b = heapq.heappop(q)
        ans += a
        heapq.heappush(q, (a + b, b))
    return ans


assert (solve(1, 1, [(1, 1)]) == 1)
assert (solve(1, 2, [(1, 1)]) == 3)

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, K, ABs))
