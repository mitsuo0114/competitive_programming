class Node:
    def __init__(self, i):
        self.i = i
        self.nexts = []

    def add(self, n, v):
        self.nexts.append((n, v))


def solve(N, M, ABCs):
    # print(N, ",", M, ",", ABCs)
    nodes = [Node(i) for i in range(0, N + 1)]
    max_v = sum([abc[2] for abc in ABCs if abc[2] > 0]) + 1

    for a, b, c in ABCs:
        nodes[a].add(b, c)

    scores = [-(10 ** 9 * 2000) - 1 for _ in range(0, N + 1)]
    visited_count = [0 for _ in range(0, N + 1)]

    q = [1]
    scores[1] = 0
    while len(q):
        index = q.pop()
        if scores[index] > max_v:
            return "inf"
        if visited_count[index] > (M + N):
            break
        visited_count[index] += 1
        for n, v in nodes[index].nexts:
            n_score = scores[index] + v
            if n_score > scores[n]:
                scores[n] = n_score
                q.insert(0, n)
    return scores[N]


assert (solve(2, 2, [(1, 2, 1), (2, 1, 1)]) == "inf")
assert (solve(2, 2, [(1, 2, -1), (2, 1, -1)]) == -1)
assert (solve(2, 2, [(1, 2, -1), (2, 1, 1)]) == -1)
assert (solve(2, 2, [(1, 2, 1), (2, 1, -1)]) == 1)
assert (solve(2, 2, [(1, 2, 0), (2, 1, 1)]) == "inf")
assert (solve(2, 2, [(1, 2, 1), (2, 1, 0)]) == "inf")
assert (solve(2, 2, [(1, 2, -1), (2, 1, 0)]) == -1)
assert (solve(2, 2, [(1, 2, 0), (2, 1, 0)]) == 0)
assert (solve(2, 2, [(1, 2, 0), (1, 2, 1)]) == 1)
assert (solve(2, 2, [(1, 2, 2), (1, 2, 1)]) == 2)
assert (solve(3, 3, [(1, 2, 1), (2, 3, 1), (3, 1, 1)]) == "inf")
assert (solve(3, 3, [(1, 2, -1), (2, 3, 1), (3, 1, 1)]) == "inf")
assert (solve(3, 3, [(1, 2, -1), (2, 3, -1), (3, 1, 1)]) == -2)
assert (solve(4, 4, [(1, 2, -1), (2, 3, -1), (3, 4, 1), (4, 1, 1)]) == -1)
assert (solve(4, 4, [(1, 2, -1), (2, 3, -1), (3, 4, 1), (4, 1, 2)]) == "inf")
assert (solve(4, 4, [(1, 4, -1), (1, 4, 1), (1, 4, 3), (1, 4, 4)]) == 4)
assert (solve(3, 3, [(1, 2, -1), (2, 3, 1), (3, 1, -1)]) == 0)
assert (solve(3, 3, [(1, 2, 4), (2, 3, 3), (1, 3, 5)]) == 7)
assert (solve(6, 5, [(1, 2, -1000000000), (2, 3, -1000000000), (3, 4, -1000000000), (4, 5, -1000000000),
                     (5, 6, -1000000000)]) == -5000000000)
print("OK")

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    ABCs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, M, ABCs))
