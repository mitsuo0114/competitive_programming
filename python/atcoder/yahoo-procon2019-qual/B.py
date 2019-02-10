from collections import Counter


def solve(ABs):
    ac = Counter([a for (a, b) in ABs] + [b for (a, b) in ABs])
    if "".join(sorted([str(v) for v in ac.values()])) == "1122":
        return "YES"
    else:
        return "NO"


assert (solve([(1, 2), (2, 3), (3, 4)]) == "YES")
assert (solve([(1, 2), (2, 3), (3, 1)]) == "NO")
assert (solve([(1, 2), (2, 3), (4, 3)]) == "YES")
assert (solve([(1, 2), (2, 3), (1, 3)]) == "NO")
assert (solve([(1, 3), (4, 3), (4, 2)]) == "YES")
assert (solve([(1, 3), (1, 2), (1, 4)]) == "NO")
assert (solve([(1, 3), (1, 2), (1, 4)]) == "NO")
assert (solve([(1, 4), (2, 3), (2, 4)]) == "YES")

if __name__ == "__main__":
    ABs = [tuple(map(int, input().split(" "))) for _ in range(3)]
    print(solve(ABs))
