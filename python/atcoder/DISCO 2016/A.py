import math
def solve(R, C):
    ans = 0
    for x in range(1, math.ceil(R/C)):
        n = math.floor(math.pow(R ** 2 - (x * C) ** 2, 0.5) / C)
        ans += n
    return ans * 4


assert (solve(1, 1) == 0)
assert (solve(2, 1) == 4)
assert (solve(3, 1) == 4 * 4)
assert (solve(15, 4) == 32)

if __name__ == "__main__":
    R, C = map(int, input().split(" "))
    print(solve(R, C))
