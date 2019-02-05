from collections import Counter


def solve(N, K, As):
    c = Counter(As)
    if len(c) <= K:
        return 0
    m = sorted([(v, k) for (k, v) in c.items()], reverse=True)
    return sum([n[0] for n in m[K:]])


if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    As = list(map(int, input().split(" ")))
    print(solve(N, K, As))
