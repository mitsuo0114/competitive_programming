
class Node:
    def __init__(self):
        self.parent = self

    def root(self):
        if self.parent == self:
            return self
        else:
            r = self.parent.root()
            self.parent = r
            return r

    def unite(self, other):
        self.parent = other.root()

    def is_unite(self, other):
        return self.root() == other.root()

def solve(N, Q, PABs):
    nodes = [Node() for _ in range(N)]
    ans = []
    for (p, a, b) in PABs:
        if p == 0:
            nodes[a].unite(nodes[b])
        else:
            ans.append("Yes" if nodes[a].is_unite(nodes[b]) else "No")
    return "\n".join(ans)


if __name__ == "__main__":
    N, Q = map(int, input().split(" "))
    PABs = []
    for _ in range(Q):
        PABs.append(map(int, input().split(" ")))
    print(solve(N, Q, PABs))
