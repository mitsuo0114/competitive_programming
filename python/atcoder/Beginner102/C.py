import math


def solve(N, As):
    As = [a - (i + 1) for i, a in enumerate(As)]
    high = 10 ** 10
    low = -10 ** 10
    ans = -10 ** 20
    while True:
        b = (high + low) // 2
        tans1 = sum(abs(a - b) for a in As)
        tans2 = sum(abs(a - b + 1) for a in As)
        if low == b:
            return min(tans1, tans2)

        if tans1 > tans2:
            high = b
        elif tans1 < tans2:
            low = b
        else:
            return min(tans1, tans2)
    #
    # b1 = math.floor(sum(As) / N)
    # b2 = math.ceil(sum(As) / N)
    # ans2 = min(sum(abs(a - b1) for a in As),
    #            sum(abs(a - b2) for a in As)
    #            )
    # assert (ans1 == ans2)
    # return ans2


assert (solve(2, [-2, -1]) == 0)
assert (solve(2, [-199, -98]) == 100)
assert (solve(2, [2, 1]) == 2)
assert (solve(2, [1, 2]) == 0)
assert (solve(5, [2, 2, 3, 5, 5]) == 2)
assert (solve(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0)
assert (solve(7, [1, 1, 1, 1, 2, 3, 4]) == 6)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
