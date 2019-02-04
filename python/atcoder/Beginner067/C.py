def solve(N, As):
    d = 0
    s = sum(As)
    m = 10 ** 15
    for a in As[:N - 1]:
        d += a
        m = min(m, abs(d - (s - d)))
    return abs(m)


assert (solve(2, [1, 2]) == 1)
assert (solve(2, [2, 1]) == 1)
assert (solve(2, [-2, -1]) == 1)
assert (solve(2, [-1, -2]) == 1)
assert (solve(6, [1, 2, 3, 4, 5, 6]) == 1)
assert (solve(6, [1, 2, 3, 4, 5, 6][::-1]) == 1)
assert (solve(2, [10, 10]) == 0)
assert (solve(2, [-10, 10]) == 20)
assert (solve(2, [10, -10]) == 20)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
