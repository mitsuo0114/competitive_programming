def solve(N, As):
    As = [1 if a % 2 == 1 else 2 for a in As]
    if all(a == 2 for a in As):
        return "second"
    else:
        return "first"

assert (solve(1, [1]) == "first")
assert (solve(1, [2]) == "second")
assert (solve(1, [3]) == "first")

assert (solve(2, [1, 1]) == "first")
assert (solve(2, [2, 1]) == "first")
assert (solve(2, [1, 2]) == "first")
assert (solve(2, [2, 2]) == "second")

assert (solve(3, [1, 1, 1]) == "first")
assert (solve(3, [2, 1, 1]) == "first")
assert (solve(3, [2, 2, 1]) == "first")
assert (solve(3, [2, 2, 2]) == "second")

assert (solve(4, [1, 1, 1, 1]) == "first")
assert (solve(4, [2, 1, 1, 1]) == "first")
assert (solve(4, [2, 2, 1, 1]) == "first")
assert (solve(4, [2, 2, 2, 1]) == "first")
assert (solve(4, [2, 2, 2, 2]) == "second")

if __name__ == "__main__":
    N = int(input())
    As = [int(input()) for _ in range(N)]
    print(solve(N, As))
