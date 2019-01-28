import math

MAX_N = 2 * 10 ** 5
fact_table = [1] * MAX_N
R = 10 ** 9 + 7

def fact(N):
    return fact_table[N]

for i in range(1, MAX_N):
    fact_table[i] = i * fact_table[i - 1] % R

def solve(H, W, A, B):
    ans = 0

    p1_y = fact(H - 1 - A)
    d2_y = fact(H - 1 - (H - A))

    for i in range(0, W - B):
        p1 = (B + i, H - 1 - A)
        p2 = (B + i, H - A)
        e = (W - 1, H - 1)
        d2 = (e[0] - p2[0], e[1] - p2[1])

        way1 = (fact(p1[0] + p1[1]) // fact(p1[0]) // p1_y)
        way3 = (fact(d2[0] + d2[1]) // fact(d2[0]) // d2_y)
        ans += (way1 % R) * (way3 % R)
    return ans % R


assert (solve(2, 2, 1, 1) == 1)
assert (solve(4, 4, 2, 2) == 6 + 4)
assert (solve(2, 3, 1, 1) == 2)
assert (solve(10, 7, 3, 4) == 3570)
print("OK")
assert (solve(100000, 100000, 99999, 99999) == 1)
print("OK")
assert (solve(100000, 100000, 44444, 55555) == 738162020)
print("OK")

if __name__ == "__main__":
    H, W, A, B = map(int, input().split(" "))
    print(solve(H, W, A, B))
