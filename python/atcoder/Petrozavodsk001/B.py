import math


def solve(N, As, Bs):
    sa = sum(As)
    sb = sum(Bs)
    if sa > sb:
        return "No"
    splus = sum([math.ceil((b - a) / 2) for a, b in zip(As, Bs) if b - a >= 0])
    if sa + splus > sb:
        return "No"
    else:
        return "Yes"


assert (solve(2, [10, 0], [10, 0]) == "Yes")
assert (solve(2, [9, 0], [10, 0]) == "Yes")
assert (solve(2, [1, 0], [2, 0]) == "Yes")
assert (solve(2, [1, 0], [1, 1]) == "Yes")
assert (solve(2, [1, 0], [2, 0]) == "Yes")
assert (solve(2, [1, 0], [2, 1]) == "Yes")
assert (solve(2, [1, 0], [2, 2]) == "Yes")
assert (solve(2, [20, 1], [24, 0]) == "Yes")
assert (solve(2, [20, 0], [24, 0]) == "Yes")
assert (solve(2, [1, 0, 1], [1, 1, 1]) == "Yes")
assert (solve(2, [1, 0, 1], [2, 1, 1]) == "Yes")
assert (solve(2, [0, 0, 3], [10, 2, 1]) == "Yes")

assert (solve(3, [1, 2, 3], [5, 2, 2]) == "Yes")
assert (solve(5, [3, 1, 4, 1, 5], [2, 7, 1, 8, 2]) == "No")
assert (solve(5, [3, 1, 5], [2, 8, 2]) == "No")
assert (solve(5, [3, 7], [2, 8]) == "No")
assert (solve(5, [4, 6], [2, 8]) == "No")
assert (solve(5, [2, 7, 1, 8, 2], [3, 1, 4, 1, 5]) == "No")

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    Bs = list(map(int, input().split(" ")))
    print(solve(N, As, Bs))
