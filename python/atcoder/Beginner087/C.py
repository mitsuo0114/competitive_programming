def solve(N, A1s, A2s):
    m = 0
    for k in range(0, N):
        m = max(m, sum(A1s[:k + 1]) + sum(A2s[k:]))
    return m


assert (solve(3, [1, 1, 0], [0, 1, 1]) == 4)
assert (solve(3, [1, 1, 0], [0, 0, 1]) == 3)
assert (solve(3, [1, 1, 0], [1, 0, 1]) == 3)
assert (solve(3, [1, 1, 1], [1, 1, 1]) == 4)

if __name__ == "__main__":
    N = int(input())
    A1s = list(map(int, input().split(" ")))
    A2s = list(map(int, input().split(" ")))
    print(solve(N, A1s, A2s))
