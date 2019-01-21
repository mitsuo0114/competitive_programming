def solve(H, W, Ss):
    d = [[-1 for __ in range(W)] for _ in range(H)]

    index = 0
    for (sh, sw) in [(h, w) for h in range(0, H) for w in range(0, W)]:
        if d[sh][sw] == -1:
            que = [(sh, sw)]
            index += 1
            d[sh][sw] = index

            while len(que):
                h, w = que.pop()
                for (hi, wi) in [(h + 1, w), (h - 1, w), (h, w - 1), (h, w + 1)]:
                    if 0 <= hi < H and 0 <= wi < W:
                        if Ss[hi][wi] != Ss[h][w] and d[hi][wi] == -1:
                            que.append((hi, wi))
                            d[hi][wi] = index
    c = [[0, 0] for _ in range(index + 1)]
    for h in range(0, H):
        for w in range(0, W):
            if Ss[h][w] == ".":
                c[d[h][w]][0] += 1
            elif Ss[h][w] == "#":
                c[d[h][w]][1] += 1
    ans = sum([b * w for (w, b) in c])
    return ans


assert (solve(2, 4, ['....', '....']) == 0)
assert (solve(3, 4, ['....', '####', '....']) == 8)
assert (solve(2, 2, ['.#', '#.']) == 4)
assert (solve(2, 3, ['###', '...']) == 3)
assert (solve(2, 3, ['...', '###']) == 3)
assert (solve(4, 3, ['###', '###', '...', '###']) == 6)
assert (solve(3, 3, ['.#.', '..#', '#..']) == 10)

if __name__ == "__main__":
    H, W = tuple(map(int, input().split(" ")))
    Ss = list([input() for l in range(H)])
    print(solve(H, W, Ss))
