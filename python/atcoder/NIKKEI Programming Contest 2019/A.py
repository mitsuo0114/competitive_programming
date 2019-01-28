def solve(N, A ,B):
    return "%d %d" % (min(A, B), max(0, A+B-N))

if __name__ == "__main__":
    N, A, B = map(int, input().split(" "))
    print(solve(N, A, B))
