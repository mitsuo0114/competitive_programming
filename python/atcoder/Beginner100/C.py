def solve(N, As):
    def f(n):
        c = 0
        while n % 2 == 0:
            c += 1
            n //= 2
        return c
    return sum([f(a) for a in As])



assert (solve(1, [2]) == 1)
assert (solve(2, [2, 2]) == 2)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
