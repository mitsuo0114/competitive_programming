from collections import Counter


def factor(N):
    ret = []
    i = 2
    while N > 1:
        if N % i == 0:
            ret.append(i)
            N //= i
        else:
            i += 1
    return ret


assert (factor(4) == [2, 2])
assert (factor(2) == [2])
assert (factor(3) == [3])
assert (factor(10) == [2, 5])


def solve(N, As):
    iter = Counter(factor(min(As)))

    for a in As:
        for k, v in iter.items():
            if a % k != 0:
                iter[k] = 0
            else:
                count = 0
                kk = k
                while a % kk == 0:
                    kk *= k
                    count += 1
                iter[k] = min(v, count)
    d = 1
    for k, v in iter.items():
        if v != 0:
            d *= k ** v
    return d


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
