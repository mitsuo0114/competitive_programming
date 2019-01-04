def solve(N, M, PYs):
    Ys = {i + 1: 1 for i in range(N)}
    ret = {}
    for p, y in sorted(PYs, key=lambda x: x[1]):
        ret[(p, y)] = "{:06d}{:06d}".format(p, Ys[p])
        Ys[p] += 1
    return [ret[(p, y)] for (p, y) in PYs]

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    PYs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print("\n".join(solve(N, M, PYs)))
