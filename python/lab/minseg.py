import random
N = 512
INT_MAX = 65536
class MinSegmentTree:

    def __init__(self, A):
        self.tree = [INT_MAX for _ in range(0, 2 * N + 1) ]
        for i, x in enumerate(A):
            self.update(i, x)

    def update(self, i, x):
        i += N - 1
        self.tree[i] = min(self.tree[i], x)
        while(i > 0):
            i = int((i - 1) / 2)
            self.tree[i] = min(self.tree[i], x)

    def minQuery(self, a, b, k, l, r):
        if b <= l or r <= a:
            return INT_MAX
        elif a <= l and r <= b:
            return self.tree[k]
        else:
            return min( self.minQuery(a, b, 2 * k + 1, l, int((l+r) / 2)),
                        self.minQuery(a, b, 2 * k + 2, int((l+r)/2), r))



for t in range(0, 1000):
    A = [int(random.random() * 100) for i in range(0, N)]
    minTree = MinSegmentTree(A)
    s = int(random.random() * N)
    e = s + int(random.random() * (N-s-1)) + 1
    mini = min(A[s:e])

    ret = minTree.minQuery(s, e, 0, 0, N)
    if mini != ret :
        print("Failed!!!!!!!")
        print(minTree.minQuery(s, e, 0, 0, N))
        print(mini)
        break


