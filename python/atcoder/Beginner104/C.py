def solve(D, G, PCs):
    # print(D, ",", G, ",", PCs)
    ans = 10000
    for d in range(0, 2 ** D):
        b = "{:011b}".format(d)[::-1][:D]
        k = 0
        point = 0
        for i, c in enumerate(b):
            if c == "1":
                k += PCs[i][0]
                point += PCs[i][1] + ((i + 1) * 100 * PCs[i][0])
        if point >= G:
            ans = min(ans, k)
            continue

        for i, (p, c) in enumerate(PCs[::-1]):
            if b[D - (i + 1)] == "1":
                continue
            for _ in range(p):
                point += (D - i) * 100
                k += 1
                if point >= G:
                    break
            if point >= G:
                break
        ans = min(ans, k)
    return ans


assert (solve(1, 300, [(1, 300)]) == 1)
assert (solve(1, 600, [(2, 600)]) == 2)
assert (solve(2, 200, [(10, 100), (1, 100)]) == 1)
assert (solve(2, 300, [(10, 100), (1, 100)]) == 1)

assert (solve(2, 1200, [(10, 0), (1, 0)]) == 11)
assert (solve(2, 1200, [(10, 0), (10, 0)]) == 6)
assert (solve(2, 1200, [(15, 0), (1, 0)]) == 11)

assert (solve(2, 1200, [(10, 0), (1, 10000)]) == 1)
assert (solve(2, 1200, [(10, 0), (10, 10000)]) == 6)
assert (solve(2, 1200, [(15, 0), (0, 0)]) == 12)

assert (solve(2, 700, [(3, 500), (5, 800)]) == 3)
assert (solve(2, 2000, [(3, 500), (5, 800)]) == 7)
assert (solve(2, 400, [(3, 500), (5, 800)]) == 2)
assert (solve(5, 25000, [(20, 1000), (40, 1000), (50, 1000), (30, 1000), (1, 1000)]) == 66)

if __name__ == "__main__":
    D, G = tuple(map(int, input().split(" ")))
    PCs = [tuple(map(int, input().split(" "))) for _ in range(D)]
    print(solve(D, G, PCs))
