def solve(N, K, ABs):
    counts = {i: 0 for i in range(1, 10 ** 5 + 1)}
    for a, b in ABs:
        counts[a] += b
    s = 0
    for c, count in counts.items():
        s += count
        if K <= s:
            return c


if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    ABs = []
    for _ in range(N):
        ABs.append(tuple(map(int, input().split(" "))))
    print(solve(N, K, ABs))
