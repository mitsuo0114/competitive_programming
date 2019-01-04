def solve(N, Ps):
    return sum(Ps) - (max(Ps) // 2)

if __name__ == "__main__":
    N = int(input())
    Ps = [int(input()) for _ in range(N)]
    print(solve(N, Ps))
