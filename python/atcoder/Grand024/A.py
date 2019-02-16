def solve(A, B, C, K):
    if K % 2 == 0:
        return A - B
    else:
        return B - A


def slow_solve(A, B, C, K):
    for _ in range(K):
        A, B, C = B + C, C + A, A + B

    return A - B


assert (slow_solve(1, 1, 1, 1) == solve(1, 1, 1, 1))
assert (slow_solve(2, 1, 1, 1) == solve(2, 1, 1, 1))
assert (slow_solve(1, 2, 1, 1) == solve(1, 2, 1, 1))
assert (slow_solve(2, 2, 1, 1) == solve(2, 2, 1, 1))
assert (slow_solve(2, 2, 2, 1) == solve(2, 2, 2, 1))
assert (slow_solve(2, 1, 1, 2) == solve(2, 1, 1, 2))
assert (slow_solve(1, 2, 1, 2) == solve(1, 2, 1, 2))
assert (slow_solve(2, 2, 1, 2) == solve(2, 2, 1, 2))
assert (slow_solve(2, 2, 2, 2) == solve(2, 2, 2, 2))
assert (slow_solve(2, 1, 1, 20) == solve(2, 1, 1, 20))
assert (slow_solve(1, 2, 1, 20) == solve(1, 2, 1, 20))
assert (slow_solve(2, 2, 1, 20) == solve(2, 2, 1, 20))
assert (slow_solve(2, 2, 2, 20) == solve(2, 2, 2, 20))
# slow_solve(2, 2, 2, 4)
# slow_solve(2, 1, 2, 4)
# slow_solve(2, 2, 1, 4)
# slow_solve(1, 2, 2, 4)
# slow_solve(5, 2, 5, 4)
slow_solve(2, 5, 7, 4)

if __name__ == "__main__":
    A, B, C, K = tuple(map(int, input().split(" ")))
    print(solve(A, B, C, K))
