def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


assert (gcd(10, 3) == 1)


def solve(N, As):
    k = min(As)
    for a in As:
        k = gcd(k, a)
    return k


assert (solve(1, [1]) == 1)
assert (solve(2, [3, 4]) == 1)
assert (solve(2, [4, 8]) == 4)
assert (solve(2, [4, 7]) == 1)
assert (solve(4, [2, 10, 8, 40]) == 2)
assert (solve(4, [5, 13, 8, 1000000000]) == 1)
assert (solve(3, [1000000000, 1000000000, 1000000000]) == 1000000000)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
