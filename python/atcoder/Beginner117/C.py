def psolve(k, Xs, N):
    arr = [[]]
    i = Xs[0]
    for x in Xs:
        if x <= i + k:
            arr[-1].append(x)
        else:
            arr.append([])
            arr[-1].append(x)
            i = x
            if len(arr) > N:
                break

    if len(arr) <= N:
        ans = sum([max(a) - min(a) for a in arr])
        return ans
    else:
        return 10 ** 9


def __solve(N, M, Xs):
    Xs = sorted(Xs)
    ans = 10 ** 9
    for k in range(0, ((Xs[-1] - Xs[0]) + 1) // N + 1):
        nans = psolve(k, Xs, N)
        ans = min(ans, nans)
    return ans

def solve(N, M, Xs):
    Xs = sorted(Xs)
    diffs = sorted([Xs[i+1] - Xs[i] for i in range(M-1)], reverse=True)
    return Xs[-1] - Xs[0] - sum(diffs[:N-1])



assert (solve(1, 2, [1, 3]) == 2)
assert (solve(1, 2, [1, 4]) == 3)
assert (solve(2, 2, [1, 4]) == 0)
assert (solve(2, 3, [1, 2, 100]) == 1)
assert (solve(2, 4, [1, 2, 101, 102]) == 2)
assert (solve(2, 4, [1, 3, 101, 103]) == 4)
assert (solve(2, 4, [1, 3, 100, 103]) == 5)
assert (solve(2, 5, [1, 2, 10, 12, 14]) == 5)
assert (solve(1, 2, [1, 4]) == 3)
assert (solve(3, 7, [-10, -3, 0, 9, -100, 2, 17]) == 19)
assert (solve(100, 1, [-100000]) == 0)

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    Xs = list(map(int, input().split(" ")))
    print(solve(N, M, Xs))
