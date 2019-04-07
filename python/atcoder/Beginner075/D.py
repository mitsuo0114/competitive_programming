from itertools import combinations


def slow_solve(N, K, XYs):
    ans = 10 ** 19 + 1
    for candidate in combinations(XYs, r=K):
        candidate = list(candidate)
        xs = sorted([x for x, y in candidate])
        max_x = xs[-1]
        min_x = xs[0]
        ys = sorted([y for x, y in candidate])
        max_y = ys[-1]
        min_y = ys[0]

        ans = min(ans, abs(max_x - min_x) * abs(max_y - min_y))
    return ans


def solve(N, K, XYs):
    ans = 10 ** 19 + 1

    XYs.sort(key=lambda x: x[0])
    for i in range(N):
        for j in range(i+K-1, N):
            narrowedXY = XYs[i:j+1]
            narrowedXY.sort(key=lambda x: x[1])
            for y1 in range(len(narrowedXY)):
                for y2 in range(y1+K, len(narrowedXY)+1):
                    min_x = XYs[i][0]
                    max_x = XYs[j][0]
                    ys = [xy[1] for xy in narrowedXY[y1:y2]]
                    max_y = max(ys)
                    min_y = min(ys)
                    ans = min(ans, abs(max_x - min_x) * abs(max_y - min_y))

    return ans

assert (solve(4, 4, [(4, 1), (3, 2), (2, 3), (1, 4)]) == 9)
assert (solve(5, 4, [(8, 1), (6, 2), (3, 3), (1, 4), (100, 100)]) == 21)
assert (solve(5, 4, [(8, 1), (6, 2), (3, 3), (1, 4), (-100, -100)]) == 21)

assert (solve(4, 2, [(4, 10), (3, 30), (2, 60), (1, 100)]) == 20)
assert (solve(4, 2, [(4, 10), (3, 50), (2, 60), (1, 100)]) == 10)
assert (solve(4, 2, [(4, 10), (3, 50), (2, 60), (1, 51)]) == 2)
assert (solve(4, 3, [(4, 10), (3, 50), (2, 60), (1, 51)]) == slow_solve(4, 3, [(4, 10), (3, 50), (2, 60), (1, 51)]))
assert (solve(4, 2, [(-4, -10), (-3, -50), (-2, -60), (-1, -100)]) == 10)
assert (solve(4, 2, [(-4, -10), (-3, -50), (-2, -60), (-1, -51)]) == 2)
assert (solve(4, 4, [(4, -1), (3, -2), (2, -3), (1, -4)]) == 9)
assert (solve(4, 4, [(4, -1), (3, -2), (2, -3), (1, -4)]) == 9)
assert (solve(4, 2, [(-4, 1), (-3, 2), (-2, 3), (-1, 4)]) == 1)

for arg in [(4, 2, [(-4, 1), (-3, 2), (-2, 3), (-1, 4)]),
            (4, 3, [(-4, 1), (-3, 2), (-2, 3), (-1, 4)]),
            (4, 4, [(-4, 1), (-3, 2), (-2, 3), (-1, 4)]),
            (4, 3, [(-4, 100), (-3, 20), (-2, 3), (-1, 4)]),
            (4, 2, [(1, 1), (3, 3), (2, 100), (100, 2)]),
            ]:
    assert(solve(*arg) == slow_solve(*arg))

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    XYs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, K, XYs))
