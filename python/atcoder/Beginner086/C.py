import math


def solve(N, TXYs):
    now = 0
    p = (0, 0)
    for t, x, y in TXYs:
        td = t - now
        dd = abs(p[0] - x) + abs(p[1] - y)
        if td % 2 != dd % 2 or td < dd:
            return "No"
        now = t
        p = (x, y)
    return "Yes"


assert (solve(1, [(1, 1, 0)]) == "Yes")
assert (solve(1, [(1, 1, 1)]) == "No")
assert (solve(1, [(2, 1, 1)]) == "Yes")
assert (solve(1, [(3, 1, 1)]) == "No")
assert (solve(1, [(4, 1, 1)]) == "Yes")
assert (solve(1, [(4, 1, 1), (6, 0, 0)]) == "Yes")
assert (solve(1, [(4, 1, 1), (6, 1, 0)]) == "No")
assert (solve(1, [(4, 1, 1), (6, 1, 1)]) == "Yes")

if __name__ == "__main__":
    N = int(input())
    TXYs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, TXYs))
