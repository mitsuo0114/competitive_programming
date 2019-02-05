def solve(N, Fs, Ps):
    profit = - 10 ** 10
    for k in range(1, 1025):
        b = "{:010b}".format(k)
        p = 0
        for P, F in zip(Ps, Fs):
            p += P[sum(F[i] * int(b[i]) for i in range(10))]
        profit = max(profit, p)
    return profit


assert (solve(1, [(1, 1, 0, 1, 0, 0, 0, 1, 0, 1)], [(3, 4, 5, 6, 7, 8, 9, -2, -3, 4, -2)]) == 8)

if __name__ == "__main__":
    N = int(input())
    Fs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    Ps = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, Fs, Ps))
