def solve(N, A, B):
    d2 = B - A - 1

    if d2 % 2 == 1:
        return "Alice"
    else:
        return "Borys"


assert (solve(2, 1, 2) == "Borys")
assert (solve(3, 1, 3) == "Alice")
assert (solve(3, 1, 2) == "Borys")
assert (solve(3, 2, 3) == "Borys")
assert (solve(4, 1, 4) == "Borys")
assert (solve(4, 1, 2) == "Borys")
assert (solve(5, 1, 5) == "Alice")
assert (solve(7, 2, 5) == "Borys")
assert (solve(6, 1, 4) == "Borys")

if __name__ == "__main__":
    N, A, B = tuple(map(int, input().split(" ")))
    print(solve(N, A, B))
