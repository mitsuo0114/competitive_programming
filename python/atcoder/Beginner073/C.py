from collections import Counter


def solve(N, As):
    c = Counter(As)
    return len([k for k, v in c.items() if v % 2 == 1])


if __name__ == "__main__":
    N = int(input())
    As = [int(input()) for _ in range(N)]
    print(solve(N, As))
