memos = {}
nines = [9 ** n for n in range(1, 6)]
sixs = [6 ** n for n in range(1, 7)]


def solve(N):
    if N < 6:
        return N
    if N in memos:
        return memos[N]
    n = 10 ** 9
    if N >= 9:
        nine_max = max(n for n in nines if n <= N)
        if N % nine_max == 0:
            n = min(n, N // nine_max)
        else:
            n = min(n, solve(N - nine_max) + 1)

    six_max = max(n for n in sixs if n <= N)
    if N % six_max == 0:
        n = min(n, N // six_max)

    memos[N] = min(n, solve(N - six_max) + 1)
    return memos[N]


assert (solve(6 + 9 * 2) == 3)
assert (solve(6 + 9 * 2 + 1) == 4)
assert (solve(6 + 9 * 2 + 2) == 5)

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
