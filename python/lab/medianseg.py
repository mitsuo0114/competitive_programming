import statistics
import random
N = 32

X_MAX = 10
class MedianSegmentTree():

    def __init__(self, A):
        self.tree = [{i : 0 for i in range(0, X_MAX)} for _ in range(0, 2 * N + 1)]
        for i, x in enumerate(A):
            self.update(i, x)
    # 3分木

    def update(self, i, x):
        i += N - 1
        self.tree[i][x] += 1
        while(i > 0):
            i = int((i - 1) / 2)
            self.tree[i][x] += 1

    def medianQuery(self, a, b, k, l, r):
        if b <= l or r <= a:
            return {}
        elif a <= l and r <= b:
            return self.tree[k]
        else:
            ltree = self.medianQuery(a, b, k * 2 + 1, l , int((l+r) / 2))
            rtree = self.medianQuery(a, b, k * 2 + 2, int((l + r) / 2), r)
            ret = {}
            for k, v in ltree.items():
                ret.setdefault(k, 0)
                ret[k] += v
            for k, v in rtree.items():
                ret.setdefault(k, 0)
                ret[k] += v
            return ret




for t in range(0, 100):
    size = int(random.random() * N / 2) + 11
    A = [int(random.random() * X_MAX) for i in range(0, size + 1)]
    medianTree = MedianSegmentTree(A)
    s = 0 #int(random.random() * size)
    e = 7 # s + int(random.random() * (size-s-1)) + 1
    total = statistics.median(A[s:e])

    appearcount = medianTree.medianQuery(s, e, 0, 0, N)

    for a in A[s:e]:
        count = len([d for d in A[s:e] if d == a])
        if appearcount[a] != count:
            print(f"Count failed {a}. should be {count} but {appearcount[a]}")
    totalcount = sum(appearcount.values())
    median = -1
    if totalcount % 2 == 1:
        # odd
        count = 0
        border = (totalcount - 1) / 2
        for k in sorted(appearcount.keys()):
            v = appearcount[k]

            if count <= border < count + v:
                ans = k
                break
            count += v
    else:
        pass
        # even

    if ans != total :
        print("Failed!!!!!!!")
        # print(medianTree.avgQuery(s, e, 0, 0, N))
        print(total)
        print(ans)
        break

