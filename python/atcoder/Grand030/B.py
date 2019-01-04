class obj():
    def __init__(self, x):
        self.x = x
        self.previous = None
        self.next = None

    def __str__(self):
        return "%d (previous : %d, next : %d" % (self.x, self.previous.x, self.next.x)

def solve(L, N, Xs):
    linkedlist = [obj(0)]
    for x in Xs:
        o = obj(x)
        if len(linkedlist):
            o.previous = linkedlist[-1]
            linkedlist[-1].next = o
        linkedlist.append(o)
    linkedlist[0].previous = linkedlist[-1]
    linkedlist[-1].next = linkedlist[0]

    def dfs(i, taken, is_previous):
        if len(taken) == N + 1:
            return 0
        if is_previous:
            pp = i.previous
            p_d = i.x - pp.x if pp.x < i.x else L - pp.x + i.x
            tmp = pp.next
            pp.next = i.next
            p = dfs(pp, taken + [pp.x], not(is_previous)) + p_d
            pp.next = tmp
            return p
        else:
            nn = i.next
            n_d = nn.x - i.x if nn.x > i.x else L - i.x + nn.x
            tmp = nn.previous
            nn.previous = i.previous
            n = dfs(nn, taken + [nn.x], not(is_previous)) + n_d
            nn.previous = tmp
            return n

    return max(dfs(linkedlist[0], [0], True), dfs(linkedlist[0], [0], False))


def slow_solve(L, N, Xs):
    linkedlist = [obj(0)]
    for x in Xs:
        o = obj(x)
        if len(linkedlist):
            o.previous = linkedlist[-1]
            linkedlist[-1].next = o
        linkedlist.append(o)
    linkedlist[0].previous = linkedlist[-1]
    linkedlist[-1].next = linkedlist[0]
    memo = {}

    def dfs(i, taken):
        if len(taken) == N + 1:
            return 0
        key = (i.x, tuple(sorted(taken)))
        if key in memo:
            return memo[key]

        pp = i.previous
        nn = i.next
        p_d = i.x - pp.x if pp.x < i.x else L - pp.x + i.x
        n_d = nn.x - i.x if nn.x > i.x else L - i.x + nn.x

        tmp = pp.p_next
        pp.p_next = i.next
        p = dfs(pp, taken + [pp.x]) + p_d
        pp.p_next = tmp

        tmp = nn.previous
        nn.previous = i.previous
        n = dfs(nn, taken + [nn.x]) + n_d
        nn.previous = tmp
        memo[key] = max(p, n)
        return memo[key]

    return dfs(linkedlist[0], [0])


# assert (slow_solve(10, 3, [2, 7, 9]) == 15)
# assert (slow_solve(10, 6, [1, 2, 3, 6, 7, 9]) == 27)
# assert (slow_solve(314159265, 7,
#                    [21662711, 77271666, 89022761, 156626166, 160332356, 166902656, 298992265]) == 1204124749)
assert (solve(10, 3, [2, 7, 9]) == 15)
assert (solve(10, 6, [1, 2, 3, 6, 7, 9]) == 27)
assert (solve(314159265, 7,
                   [21662711, 77271666, 89022761, 156626166, 160332356, 166902656, 298992265]) == 1204124749)
print("Test OK")

if __name__ == "__main__":
    l = input().split()
    L, N = int(l[0]), int(l[1])
    Xs = [int(input()) for _ in range(N)]
    print(slow_solve(L, N, Xs))
