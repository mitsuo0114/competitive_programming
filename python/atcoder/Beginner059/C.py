def psolve(positive, As):
    i = 0
    ans = 0
    for a in As:
        if positive:
            if i + a <= 0:
                ans += abs(1 - (i + a))
                a += 1 - (i + a)
        else:
            if i + a >= 0:
                ans += abs(-1 - (i + a))
                a += -1 - (i + a)
        i += a
        positive = not positive
    return ans


def solve(N, As):
    return min(psolve(True, As), psolve(False, As))


assert (solve(1, [0]) == 1)
assert (solve(2, [0, 0]) == 3)
assert (solve(2, [0, -1]) == 2)
assert (solve(2, [0, 1]) == 2)
assert (solve(3, [0, 0, 1]) == 4)
assert (solve(3, [0, 0, -1]) == 4)
assert (solve(3, [0, 0, 0]) == 5)
assert (solve(3, [0, 0, 0, 1]) == 6)  # -1, 2, -2, 2
assert (solve(3, [0, 0, 0, -1]) == 6)  # 1, -2, 2, -2
assert (solve(1, [1]) == 0)
assert (solve(1, [-1]) == 0)
assert (solve(2, [1, 1]) == 3)
assert (solve(2, [-1, -1]) == 3)
assert (solve(2, [-1, 1]) == 1)
assert (solve(4, [1, -3, 1, 0]) == 4)
assert (solve(5, [3, -6, 4, -5, 7]) == 0)
assert (solve(6, [-1, 4, 3, 2, -5, 4]) == 8)

if __name__ == "__main__":
    n = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(n, As))
