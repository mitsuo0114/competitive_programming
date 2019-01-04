def solve(N, K, Hs):
    Hs.sort()
    return min([b - a for (a, b) in zip(Hs[:], Hs[K - 1:])])


if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    Hs = [int(input()) for _ in range(N)]
    print(solve(N, K, Hs))
