from collections import Counter


def solve(H, W, N, ABs):
    total = (H - 2) * (W - 2)
    points = {}
    for a, b in ABs:
        a -= 1
        b -= 1
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 < a + i < H - 1 and 0 < b + j < W - 1:
                    d = (a + i, b + j)
                    if d not in points:
                        points[d] = 0
                    points[d] += 1
    c = Counter([v for v in points.values()])
    ans = [total - len(points)] + [c[f] if f in c else 0 for f in range(1, 10)]
    return "\n".join([str(a) for a in ans])

#
# assert (solve(4, 5, 8, [
#     (1, 1),
#     (1, 4),
#     (1, 5),
#     (2, 3),
#     (3, 1),
#     (3, 2),
#     (3, 4),
#     (4, 4),
# ]) == "\n".join([str(a) for a in [0,
#                                   0,
#                                   0,
#                                   2,
#                                   4,
#                                   0,
#                                   0,
#                                   0,
#                                   0,
#                                   0]]))

if __name__ == "__main__":
    H, W, N = map(int, input().split(" "))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(H, W, N, ABs))
