def solve(H, W, field):
    ret = []
    for y in range(0, H):
        for x in range(0, W):
            if field[y][x] % 2 == 1:
                for (xi, yi) in [(x + 1, y), (x, y + 1)]:
                    if 0 <= xi < W and 0 <= yi < H:
                            ret.append(" ".join([str(y + 1), str(x + 1), str(yi + 1), str(xi + 1)]))
                            field[y][x] -= 1
                            field[yi][xi] += 1
                            break
    return [len(ret)] + ret

if __name__ == "__main__":
    l = input()
    H, W = int(l.split()[0]), int(l.split()[1])
    field = [[int(c) for c in input().split(" ")] for _ in range(0, H)]
    [print(l) for l in solve(H, W, field)]



import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(2, 3, [l.strip() for l in """
1 2 3
0 1 1
""".splitlines() if len(l.strip())]), [l.strip() for l in """
3
2 2 2 3
1 1 1 2
1 3 1 2
""".splitlines() if len(l.strip())])
