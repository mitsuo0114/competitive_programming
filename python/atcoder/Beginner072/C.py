from collections import Counter


def solve(N, As):
    c = Counter(As)
    c.update([a + 1 for a in As])
    c.update([a - 1 for a in As])
    return max([v for v in c.values()])

assert (solve(4, [1, 1, 2, 2]) == 4)
assert (solve(4, [2, 2, 2, 2]) == 4)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))

