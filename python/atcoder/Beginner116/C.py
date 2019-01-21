# Hs = [1, 2, 2, 1]
# assert (split(0, 4) == [(0, 4)])
# Hs = [1, 0, 2, 1]
# assert (split(0, 4) == [(0, 1), (2, 4)])
# Hs = [0, 2, 2, 1]
# assert (split(0, 4) == [(1, 4)])

def solve(N, Hs):
    def split(s, e):
        d = []
        for i in range(s, e):
            if Hs[i] != 0 and len(d) % 2 == 0:
                d.append(i)
            elif Hs[i] == 0 and len(d) % 2 == 1:
                d.append(i)
        if len(d) % 2 == 1:
            d.append(e)

        return [(d[2 * i], d[2 * i + 1]) for i in range(len(d) // 2)]

    def f(s, e):

        ans = 0
        if s >= len(Hs) or s > e:
            return 0
        if s == e:
            return Hs[s]
        m = min(Hs[s:e])
        c = Hs[s:e].count(0)
        if len(Hs[s:e]) == c:
            return 0
        if m == 0:
            l = split(s, e)
            for ss, ee in l:
                ans += f(ss, ee)
        else:
            ans += m
            for i in range(s, e):
                Hs[i] -= m
            ans += f(s, e)
        return ans

    return f(0, N)


assert (solve(4, [1, 2, 2, 1]) == 2)
assert (solve(5, [3, 1, 2, 3, 1]) == 5)
assert (solve(8, [4, 23, 75, 0, 23, 96, 50, 100]) == 221)

if __name__ == "__main__":
    N = int(input())
    Hs = list(map(int, input().split(" ")))
    print(solve(N, Hs))
