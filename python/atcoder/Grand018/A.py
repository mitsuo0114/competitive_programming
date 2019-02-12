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

from collections import Counter


def solve(N, K, As):
    if K > max(As):
        return "IMPOSSIBLE"
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

    if all([v == 0 for v in iter.values()]):
        return "POSSIBLE"
    else:
        d = 1
        for k, v in iter.items():
            if v != 0:
                d *= k ** v
        if K % d == 0:
            return "POSSIBLE"
    return "IMPOSSIBLE"


assert (solve(2, 5, [10, 15]) == "POSSIBLE")
assert (solve(2, 5, [7, 10]) == "POSSIBLE")
assert (solve(2, 5, [21, 10]) == "POSSIBLE")
assert (solve(3, 5, [6, 9, 3]) == "IMPOSSIBLE")
assert (solve(5, 12, [10, 2, 8, 6, 4]) == "IMPOSSIBLE")
assert (solve(4, 11, [11, 3, 7, 15]) == "POSSIBLE")

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    As = list(map(int, input().split(" ")))
    print(solve(N, K, As))
