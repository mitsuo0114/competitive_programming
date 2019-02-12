def solve(N, As):
    return "YES" if len([a for a in As if a % 2 == 1]) % 2 == 0 else "NO"


assert (solve(2, [2, 2]) == "YES")
assert (solve(2, [3, 3]) == "YES")
assert (solve(2, [2, 3]) == "NO")
assert (solve(2, [2, 3, 3]) == "YES")

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
