def solve(N, M, ABs):
    from1 = set()
    toN = set()
    for a, b in ABs:
        a, b = min(a, b), max(a, b)
        if a == 1:
            from1.add(b)
        if b == N:
            toN.add(a)
    return "POSSIBLE" if len(from1.intersection(toN)) else "IMPOSSIBLE"


assert (solve(3, 2, [(1, 2), (2, 3)]) == "POSSIBLE")
assert (solve(4, 3, [(1, 2), (2, 3), (3, 4)]) == "IMPOSSIBLE")
assert (solve(100000, 1, [(1, 99999)]) == "IMPOSSIBLE")
assert (solve(5, 5, [(1, 3), (4, 5), (2, 3), (2, 4), (1, 4)]) == "POSSIBLE")

if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, M, ABs))
