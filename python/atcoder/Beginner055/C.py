def solve(N, M):
    ans = min(N, M // 2)
    M -= ans * 2
    ans += M // 4
    return ans


assert (solve(1, 2) == 1)
assert (solve(1, 6) == 2)
assert (solve(1, 10) == 3)
assert (solve(2, 6) == 2)
assert (solve(3, 6) == 3)

if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    print(solve(N, M))
