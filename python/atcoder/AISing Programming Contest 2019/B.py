from itertools import combinations


def solve(N, A, B, Ps):
    q1 = len([p for p in Ps if p <= A])
    q2 = len([p for p in Ps if A + 1 <= p <= B])
    q3 = len([p for p in Ps if B + 1 <= p])
    return min(q1, q2, q3)


if __name__ == "__main__":
    N = int(input())
    A, B = tuple(map(int, input().split(" ")))
    Ps = list(map(int, input().split(" ")))
    print(solve(N, A, B, Ps))
