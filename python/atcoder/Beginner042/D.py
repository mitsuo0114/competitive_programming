import math


def solve(H, W, A, B):
    ans = 0
    R = 10 ** 9 + 7

    p1_y = math.factorial(H - 1 - A)
    d2_y = math.factorial(H - 1 - (H - A))
    way1 = -1
    way3 = -1

    for i in range(0, W - B):
        p1 = (B + i, H - 1 - A)
        p2 = (B + i, H - A)
        e = (W - 1, H - 1)
        d2 = (e[0] - p2[0], e[1] - p2[1])

        if way1 == -1:
            way1 = (math.factorial(p1[0] + p1[1]) // math.factorial(p1[0]) // p1_y)
        else:
            way1 *= (p1[0] + p1[1])
            way1 //= (p1[0])

        if way3 == -1:
            way3 = (math.factorial(d2[0] + d2[1]) // math.factorial(d2[0]) // d2_y)
        else:
            way3 *= (d2[0] + 1)
            way3 //= (d2[0] + d2[1] + 1)
        ans += (way1 % R) * (way3 % R)
    return ans % R


assert (solve(2, 2, 1, 1) == 1)
assert (solve(4, 4, 2, 2) == 6 + 4)
assert (solve(2, 3, 1, 1) == 2)
assert (solve(10, 7, 3, 4) == 3570)
assert (solve(100000, 100000, 99999, 99999) == 1)
assert (solve(100000, 100000, 44444, 55555) == 738162020)

if __name__ == "__main__":
    H, W, A, B = map(int, input().split(" "))
    print(solve(H, W, A, B))
