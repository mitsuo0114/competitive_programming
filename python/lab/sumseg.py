import random

class SumSegmentTree():
    ## 実装メモ
    ## update時は下から.

    ## 2分木において
    ## size は nのべき乗 * 2 + 1
    ## 親のindex は　自分のノードをn として (n - 1) / 2
    ## 子のindex は　自分のノードをn として 2n + 1 / 2n + 2


    def __init__(self, A):
        self.n = 256
        self.tree = [0] * (self.n* 2 + 1)
        for i, a in enumerate(A):
            self.update(i, a)

    def update(self, i, x):
        i += self.n - 1 # スタートは葉のノードに
        self.tree[i] += x
        while(i > 0):
            i = int((i - 1) / 2)
            self.tree[i] += x

    def sumQuery(self, a, b, k, l, r):
        # 区間 a - bの合計
        # k : 現在のセグメント木のindex
        # l, r はkが指すセグメント木の区間

        # 交差なし
        if (r<=a or b<=l):
            return 0
        elif (a <= l and r <= b): # 完全に含む
            # print("tree returned " + str(self.tree[k]))
            return self.tree[k]
        else:
            # 半端に含む => 子に分割
            vl = self.sumQuery(a, b, k * 2 + 1, l, int((l + r) / 2))
            vr = self.sumQuery(a, b, k * 2 + 2, int((l + r) / 2), r)
            return vl + vr

N = 256
for t in range(0, 100):
    A = [int(random.random() * 10) for i in range(0, N)]
    sumTree = SumSegmentTree(A)
    s = int(random.random() * N)
    e = s + int(random.random() * 10)

    if sumTree.sumQuery(s, e, 0, 0, sumTree.n) != sum(A[s:e]):
        print("Failed!!")
        print(A)
        print("s : " + str(s) +", e :" + str(e))
        print("tree returned : " + str(sumTree.sumQuery(s, e, 0, 0, len(A))))
        print("ans : " + str(sum(A[s:e])))
        break


