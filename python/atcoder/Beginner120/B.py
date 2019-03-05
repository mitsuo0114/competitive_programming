def solve(A, B, K):
    i = 1
    ans = []
    while i <= max(A, B):
        if A % i == 0 and B % i == 0:
            ans.append(i)
        i += 1
    return ans[::-1][K-1]


if __name__ == "__main__":
    A, B, K = tuple(map(int, input().split(" ")))
    print(solve(A, B, K))
