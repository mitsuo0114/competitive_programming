from itertools import combinations
def slow_solve(N, Xs):
    ans = 0
    for pairs in combinations(Xs, 2):
        ans += abs(pairs[0] - pairs[1])
    return ans

def solve(N, Xs):
    ans = 0
    Xs = sorted(Xs)
    for i, j in zip(range(N), range(1, N)):
        d = abs(Xs[j] - Xs[i])
        c = ((i+1) * (N-i-1))
        ans += d * c

    return ans

# import random
# N = sorted([random.randint(1, 100) for _ in range(100)])
# print(N)
# print(solve(len(N), N) == slow_solve(len(N), N))

if __name__ == "__main__":
    N = int(input())
    Xs = [int(c) for c in input().split(" ")]
    print(solve(N, Xs))
