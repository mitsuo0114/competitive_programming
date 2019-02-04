def solve(N, T, ts):
    return sum([min(ts[i + 1] - ts[i], T) for i in range(N - 1)]) + T


assert (solve(1, 1, [1]) == 1)
assert (solve(1, 2, [1]) == 2)
assert (solve(2, 2, [1, 100]) == 4)
assert (solve(2, 2, [1, 2]) == 3)
assert (solve(2, 4, [0, 3]) == 7)
assert (solve(2, 4, [0, 4]) == 8)
assert (solve(4, 1000000000, [0, 1000, 1000000, 1000000000]) == 2000000000)
assert (solve(1, 1, [0]) == 1)
assert (solve(9, 10, [0, 3, 5, 7, 100, 110, 200, 300, 311]) == 67)

if __name__ == "__main__":
    N, T = tuple(map(int, input().split(" ")))
    ts = list(map(int, input().split(" ")))
    print(solve(N, T, ts))
