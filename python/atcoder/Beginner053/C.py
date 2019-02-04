
def solve(x):
    ans = (x // 11) * 2
    x -= (ans // 2) * 11
    if x == 0:
        return ans
    elif x <= 6:
        return ans + 1
    else:
        return ans + 2


assert (solve(11) == 2)
assert (solve(12) == 3)
assert (solve(1) == 1)
assert (solve(6) == 1)
assert (solve(7) == 2)
assert (solve(10) == 2)

if __name__ == "__main__":
    x = int(input())
    print(solve(x))
