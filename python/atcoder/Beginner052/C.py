from collections import Counter


def f(N):
    d = []
    i = 2
    while N > 1:
        if N % i == 0:
            d.append(i)
            N //= i
        else:
            i += 1
    return d


assert (f(4) == [2, 2])
assert (f(6) == [2, 3])
assert (f(10) == [2, 5])
assert (f(20) == [2, 2, 5])


def solve(N):
    c = Counter()
    for k in range(2, N + 1):
        c.update(f(k))
    ans = 1
    P = 10 ** 9 + 7
    for count in c.values():
        ans *= (count + 1)
        ans %= P
    return ans


assert (solve(3) == 4)
assert (solve(6) == 30)
assert (solve(1000) == 972926972)

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
