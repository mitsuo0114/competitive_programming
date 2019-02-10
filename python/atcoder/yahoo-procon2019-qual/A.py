import math
def solve(N, K):
    return "YES" if K <= math.ceil(N / 2) else "NO"

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    print(solve(N, K))
