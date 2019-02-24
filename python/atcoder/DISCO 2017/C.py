import bisect


def solve(N, C, Ls):
    Ls = sorted(Ls)
    ans = 0
    while len(Ls):
        l = Ls.pop()
        ans += 1

        i = bisect.bisect_right(Ls, C - 1 - l)
        while i > 0:
            i -= 1
            if l + Ls[i] + 1 <= C:
                Ls.pop(i)
                break
    return ans


assert (solve(1, 1, [1]) == 1)
assert (solve(2, 10, [1, 2]) == 1)
assert (solve(2, 1, [1, 2]) == 2)
assert (solve(2, 2, [1, 2]) == 2)
assert (solve(2, 3, [1, 2]) == 2)
assert (solve(2, 4, [1, 2]) == 1)

if __name__ == "__main__":
    N, C = map(int, input().split(" "))
    Ls = [int(input()) for _ in range(N)]
    print(solve(N, C, Ls))
