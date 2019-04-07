from heapq import heappush, heappop


def solve(X, Y, Z, K, As, Bs, Cs):
    As.sort()
    Bs.sort()
    Cs.sort()
    ADs = [a2 - a1 for a1, a2 in zip(As, As[1:])][::-1]
    BDs = [a2 - a1 for a1, a2 in zip(Bs, Bs[1:])][::-1]
    CDs = [a2 - a1 for a1, a2 in zip(Cs, Cs[1:])][::-1]

    m = As[-1] + Bs[-1] + Cs[-1]
    h = []
    ans = [m]
    if ADs:
        heappush(h, (ADs[0], (0, -1, -1)))
    if BDs:
        heappush(h, (BDs[0], (-1, 0, -1)))
    if CDs:
        heappush(h, (CDs[0], (-1, -1, 0)))
    taken = set()

    for i in range(K - 1):
        p, stacks = heappop(h)
        while (p, stacks) in taken:
            p, stacks = heappop(h)
        taken.add((p, stacks))
        ans.append(m - p)

        if stacks[0] + 1 < len(ADs):
            heappush(h, ((p + ADs[stacks[0] + 1]), (stacks[0] + 1, stacks[1], stacks[2])))
        if stacks[1] + 1 < len(BDs):
            heappush(h, ((p + BDs[stacks[1] + 1]), (stacks[0], stacks[1] + 1, stacks[2])))
        if stacks[2] + 1 < len(CDs):
            heappush(h, ((p + CDs[stacks[2] + 1]), (stacks[0], stacks[1], stacks[2] + 1)))

    return "\n".join([str(a) for a in ans])


assert(solve(10, 10, 1, 100, [10] * 10, [10] * 10, [10]) == "\n".join(["30"] * 100))

if __name__ == "__main__":
    X, Y, Z, K = tuple(map(int, input().split(" ")))
    As = list(map(int, input().split(" ")))
    Bs = list(map(int, input().split(" ")))
    Cs = list(map(int, input().split(" ")))
    print(solve(X, Y, Z, K, As, Bs, Cs))
