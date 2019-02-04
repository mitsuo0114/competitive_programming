def solve(N, As, Bs, Cs):
    # print(As, Bs, Cs)
    ans = 0
    As.sort()
    Bs.sort()
    Cs.sort()

    memo = {}
    for b in Bs:
        bans = 0
        for i, c in enumerate(Cs):
            if b < c:
                bans += N - i
                break
        memo[b] = bans

    for a in As:
        for b in Bs:
            if b > a and b in memo:
                ans += memo[b]

    return ans


assert (solve(1, [1], [2], [3]) == 1)
assert (solve(2, [1, 2], [3, 4], [5, 6]) == 2 ** 3)
assert (solve(3, [1, 1, 1], [2, 2, 2], [3, 3, 3]) == 3 ** 3)
assert(solve(6, [3, 14, 159, 2, 6, 53],[58, 9, 79, 323, 84, 6],[2643, 383, 2, 79, 50, 288]) == 87)
print("OK")

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    Bs = list(map(int, input().split(" ")))
    Cs = list(map(int, input().split(" ")))
    print(solve(N, As, Bs, Cs))
