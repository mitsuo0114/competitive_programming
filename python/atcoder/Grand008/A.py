def solve(x, y):
    if y < 0 and x < 0:
        if abs(x) <= abs(y):
            return 1 + abs(y) - abs(x) + 1
        if abs(x) > abs(y):
            return abs(x) - abs(y)
    elif x >= 0 and y >= 0:
        if abs(x) <= abs(y):
            return abs(y) - abs(x)
        if abs(x) > abs(y):
            if y != 0:
                return 1 + abs(x) - abs(y) + 1
            else:
                return 1 + abs(x) - abs(y)
    elif x < 0 and y >= 0:
        if y != 0:
            return abs(abs(x) - abs(y)) + 1
        else:
            return abs(abs(x) - abs(y))
    elif x >= 0 and y < 0:
        if y != 0:
            return abs(abs(x) - abs(y)) + 1
        else:
            return abs(abs(x) - abs(y))


assert (solve(1, 2) == 1)
assert (solve(2, 1) == 1 + 1 + 1)
assert (solve(-3, 2) == 2)
assert (solve(-3, 4) == 2)
assert (solve(2, -3) == 2)
assert (solve(4, -3) == 2)

assert (solve(0, -3) == 4)
assert (solve(0, 3) == 3)
assert (solve(0, 0) == 0)
assert (solve(-3, 0) == 3)
assert (solve(3, 0) == 4)
assert (solve(-3, -5) == 1 + 2 + 1)
assert (solve(-3, -2) == 1)

if __name__ == "__main__":
    x, y = tuple(map(int, input().split(" ")))
    print(solve(x, y))
