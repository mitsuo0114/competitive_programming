
class UnionFind:
    import sys
    sys.setrecursionlimit(100000)

    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def root(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.root(self.parents[i])
            return self.parents[i]

    def unite(self, i, j):
        self.parents[self.root(self.parents[i])] = self.root(j)

    def is_unite(self, i, j):
        return self.root(i) == self.root(j)


from collections import Counter


def solve(N, M, ABs):
    uf = UnionFind(N)
    counter = Counter([i + 1 for i in range(N)])
    ans = []
    tans = N * (N - 1)
    for a, b in ABs[::-1]:
        ans.append(str(tans // 2))

        if not uf.is_unite(a, b):
            ar = uf.root(a)
            br = uf.root(b)

            tans -= counter[ar] * (N - counter[ar])
            tans -= counter[br] * (N - counter[br])
            counter[br] += counter[ar]
            tans += counter[br] * (N - counter[br])

            uf.unite(a, b)
    return "\n".join(ans[::-1])


assert (solve(2, 1, [(1, 2)]) == "1")
assert (solve(4, 5, [(1, 2), (3, 4), (1, 3), (2, 3), (1, 4)]) == "0\n0\n4\n5\n6")
assert (solve(6, 5, [(2, 3), (1, 2), (5, 6), (3, 4), (4, 5)]) == "8\n9\n12\n14\n15")

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, M, ABs))
