def solve(N, As):
    n = 1

    def gcd(a, b):
        a, b = min(a, b), max(a, b)
        while a > 0:
            a, b = b % a, a
        return b

    def lcm(a, b):
        return a * b // gcd(a, b)

    for a in As:
        n = lcm(a, n)
    return n


if __name__ == "__main__":
    N = int(input())
    As = [int(input()) for _ in range(N)]
    print(solve(N, As))
