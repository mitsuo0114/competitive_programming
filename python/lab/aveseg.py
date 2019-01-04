import random
N = 256

class AveSegmentTree():
    def __init__(self, A):
        self.n = N
        self.tree = [(0, 0) for __ in range(0, self.n * 2 + 1)]
        for i, x in enumerate(A):
            self.append(i, x)

    def append(self, i, x):
        i += self.n - 1
        c = self.tree[i]
        self.tree[i] = (c[0] + x, c[1] + 1)

        while i > 0:
            i = int((i - 1) / 2)
            c = self.tree[i]
            self.tree[i] = (c[0] + x, c[1] + 1)

    def avgQuery(self, a, b, k , l , r):
        if r <= a or b <= l: return [0, 0]
        elif a <= l and r <= b:
            return self.tree[k]
        else:
            sum1, count1 = tuple(self.avgQuery(a, b, 2 * k + 1, l, int((l + r) / 2)))
            sum2, count2 = tuple(self.avgQuery(a, b, 2 * k + 2, int((l + r) / 2), r))
            return [sum1 + sum2, count1 + count2]

for t in range(0, 100):
    A = [int(random.random() * 100) for i in range(0, N)]
    avgTree = AveSegmentTree(A)
    s = int(random.random() * N)
    e = s + int(random.random() * (N-s-1)) + 1
    total = sum(A[s:e])

    ans, count = tuple(avgTree.avgQuery(s, e, 0, 0, N))
    if ans / count  != (sum(A[s:e]) / len(A[s:e])) :
        print("Failed!!!!!!!")
        print(avgTree.avgQuery(s, e, 0, 0, N))
        print(ans / count)
        print(sum(A[s:e]), len(A[s:e]) )
        print(sum(A[s:e]) / len(A[s:e]) )
        break

