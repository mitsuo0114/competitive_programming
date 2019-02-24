from itertools import product


def solve(N, A, B, C, Ls):
    ans = 10000
    for p in product("ABCD", repeat=N):
        if "A" not in p or "B" not in p or "C" not in p:
            continue
        As = sum(Ls[i] for i in range(N) if p[i] == "A")
        Bs = sum(Ls[i] for i in range(N) if p[i] == "B")
        Cs = sum(Ls[i] for i in range(N) if p[i] == "C")
        tans = abs(As - A) + abs(Bs - B) + abs(Cs - C) + \
               (p.count("A") - 1) * 10 + (p.count("B") - 1) * 10 + (p.count("C") - 1) * 10
        ans = min(ans, tans)
    return ans


assert (solve(3, 1, 1, 1, [1, 1, 1]) == 0)
assert (solve(3, 1, 1, 1, [2, 2, 2]) == 3)
assert (solve(3, 1, 1, 1, [2, 2, 4]) == 5)
assert (solve(3, 2, 1, 1, [2, 2, 4]) == 4)
assert (solve(3, 1, 1, 2, [2, 2, 4]) == 4)

if __name__ == "__main__":
    N, A, B, C = tuple(map(int, input().split(" ")))
    Ls = [int(input()) for _ in range(N)]
    print(solve(N, A, B, C, Ls))
