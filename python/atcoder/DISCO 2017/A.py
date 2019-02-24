import math


def tsolve(R, K):
    ans = 0
    center = (R // K) % 2
    for x in range(0, (R // 2) // K):
        r = (R // 2) ** 2
        d = (R // 2 - x * K) ** 2
        a = math.floor(math.pow((r - d), 0.5) * 2 / K)
        if d == 0:
            a -= 2
        if a > 0 and a % 2 != center:
            a -= 1
        ans += a

    if center == 0:
        return ans * 2
    else:
        return ans * 2 + (R // K - 2)


assert (tsolve(200, 20) == 60)
assert (tsolve(300, 20) == 145)


def solve(K):
    return "%d %d" % (tsolve(200, K), tsolve(300, K))


assert (solve(20) == "60 145")

if __name__ == "__main__":
    K = int(input())
    print(solve(K))
