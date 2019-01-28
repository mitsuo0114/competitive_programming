import heapq


def cheat_solve(N, ABs):
    Ds = sorted([ab[0] + ab[1] for ab in ABs], reverse=True)
    bsum = sum([ab[1] for ab in ABs])
    dsum = sum(Ds[::2])
    return dsum - bsum


def solve(N, ABs):
    # print(N, ",", ABs)
    K = 10 ** 9
    taken = {i: False for i in range(N)}
    As = [(K - ab[0], K - ab[1], i) for i, ab in enumerate(ABs)]
    Bs = [(K - ab[1], K - ab[0], i) for i, ab in enumerate(ABs)]
    heapq.heapify(As)
    heapq.heapify(Bs)
    ans = 0
    taken_count = 0
    isTakahashi = True
    while True:
        if taken_count >= N:
            break

        am = As[0]
        while taken[am[2]]:
            heapq.heappop(As)
            am = As[0]

        bm = Bs[0]
        while taken[bm[2]]:
            heapq.heappop(Bs)
            bm = Bs[0]

        aTaka = K - am[0]
        bAoki = K - bm[0]

        bTaka = K - bm[1]
        aAoki = K - am[1]

        if isTakahashi:
            if aTaka > bAoki:
                ans += aTaka
                taken[am[2]] = True
                taken_count += 1
                heapq.heappop(As)
            elif aTaka < bAoki:
                ans += bTaka
                taken[bm[2]] = True
                taken_count += 1
                heapq.heappop(Bs)
            elif aTaka == bAoki:
                if aAoki < bTaka:
                    ans += bTaka
                    taken[bm[2]] = True
                    taken_count += 1
                    heapq.heappop(Bs)
                else:
                    ans += aTaka
                    taken[am[2]] = True
                    taken_count += 1
                    heapq.heappop(As)
        else:
            if aTaka > bAoki:
                ans -= aAoki
                taken[am[2]] = True
                taken_count += 1
                heapq.heappop(As)
            elif aTaka < bAoki:
                ans -= bAoki
                taken[bm[2]] = True
                taken_count += 1
                heapq.heappop(Bs)
            else:
                if aAoki < bTaka:
                    ans -= bAoki
                    taken[bm[2]] = True
                    taken_count += 1
                    heapq.heappop(Bs)
                else:
                    ans -= aAoki
                    taken[am[2]] = True
                    taken_count += 1
                    heapq.heappop(As)

        isTakahashi = not isTakahashi

    return ans


assert (cheat_solve(2, [(10, 10), (10, 20)]) == 0)
assert (cheat_solve(3, [(10, 10), (10, 20), (10, 30)]) == 0)
assert (cheat_solve(3, [(10, 30), (10, 20), (10, 10)]) == 0)
assert (cheat_solve(3, [(10, 10), (20, 10), (30, 10)]) == 30)
assert (cheat_solve(3, [(30, 10), (10, 10), (20, 30)]) == 20)
assert (cheat_solve(3, [(30, 10), (20, 10), (10, 10)]) == 30)
assert (cheat_solve(4, [(30, 0), (20, 0), (0, 30), (0, 20)]) == 0)
assert (cheat_solve(4, [(30, 0), (20, 0), (0, 40), (0, 50)]) == -10)
assert (cheat_solve(4, [(0, 30), (0, 20), (30, 0), (20, 0)]) == 0)

assert (cheat_solve(4, [(10, 10), (10, 20), (10, 30), (10, 40)]) == -20)
assert (cheat_solve(4, [(10, 40), (10, 30), (10, 20), (10, 10)]) == -20)
assert (cheat_solve(4, [(10, 10), (20, 10), (30, 10), (40, 10)]) == 40)
assert (cheat_solve(4, [(40, 10), (30, 10), (20, 10), (10, 10)]) == 40)
assert (cheat_solve(2, [(10, 10), (20, 20)]) == 10)
assert (cheat_solve(3, [(10, 10), (20, 20), (30, 30)]) == 20)
assert (cheat_solve(3, [(20, 10), (20, 20), (20, 30)]) == 20)
assert (cheat_solve(6, [(1, 1000000000), (1, 1000000000), (1, 1000000000), (1, 1000000000), (1, 1000000000),
                        (1, 1000000000)]) == -2999999997
        )
assert (cheat_solve(10 * 5, [(10, 10) for _ in range(10 * 5)]) == 0)
assert (cheat_solve(10 * 5 - 1, [(10, 10) for _ in range(10 * 5 - 1)]) == 10)
assert (cheat_solve(10 * 5, [(0, 10 ** 9) for _ in range(10 * 5)]) == -25000000000)
assert (cheat_solve(10 * 5, [(10 ** 9, 0) for _ in range(10 * 5)]) == 25000000000)
assert (cheat_solve(10 * 5, [(10 ** 9, 10 ** 9) for _ in range(10 * 5)]) == 0)
assert (cheat_solve(10 * 5, [(10 ** 9, 10 ** 9) for _ in range(10 * 5)]) == 0)

print("OK")

if __name__ == "__main__":
    N = int(input())
    ABs = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, ABs))
