def solve(N, As):
    avg = sum(As) / N
    return min([(abs(c - avg), i) for i, c in enumerate(As)])[1]

if __name__ == "__main__":
    N = int(input())
    As = [int(c) for c in input().split()]
    print(solve(N, As))
