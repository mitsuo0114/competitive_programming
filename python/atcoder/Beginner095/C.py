def solve(A, B, C, X, Y):
    ans = X * A + B * Y
    ans = min(ans, 2 * C * X + B * max(Y - X, 0))
    ans = min(ans, A * max(X - Y, 0) + 2 * C * Y)
    return ans


assert (solve(1, 0, 1000, 1, 0) == 1)
assert (solve(0, 1, 1000, 0, 1) == 1)
assert (solve(1, 1, 1000, 1, 1) == 2)
assert (solve(100, 100, 1, 1, 0) == 2)
assert (solve(100, 100, 1, 1, 1) == 2)
assert (solve(100, 100, 1, 0, 1) == 2)
assert (solve(100, 100, 1, 2, 0) == 4)
assert (solve(1, 100, 1, 2, 0) == 2)
assert (solve(3, 3, 1, 2, 2) == 4)

if __name__ == "__main__":
    A, B, C, X, Y = tuple(map(int, input().split(" ")))
    print(solve(A, B, C, X, Y))
