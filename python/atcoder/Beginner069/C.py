
def solve(N, As):
    # print(N, ",", As)
    n4 = len([n for n in As if n % 4 == 0])
    n2 = len([n for n in As if n % 4 != 0 and n % 2 == 0])
    n0 = len([n for n in As if n % 2 != 0])
    if n2 >= 2:
        return "Yes" if n4 >= n0 else "No"
    else:
        return "Yes" if (n4 + 1) >= (n0 + n2) else "No"


assert (solve(3, [1, 10, 100]) == "Yes")
assert (solve(4, [1, 2, 3, 4]) == "No")
assert (solve(3, [1, 4, 1]) == "Yes")
assert (solve(4, [1, 4, 1, 1]) == "No")
assert (solve(4, [1, 4, 1, 2]) == "No")
assert (solve(4, [1, 4, 2, 2]) == "Yes")
assert (solve(4, [2, 4, 2, 2]) == "Yes")
assert (solve(4, [1, 4, 2, 4]) == "Yes")
assert (solve(4, [2, 2, 2, 1]) == "No")
assert (solve(2, [1, 1]) == "No")
assert (solve(6, [2, 7, 1, 8, 2, 8]) == "Yes")

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
