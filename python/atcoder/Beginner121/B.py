def solve(N, M, C, Bs, As):
    ans = 0
    for adata in As:
        if sum(a * b for a, b in zip(adata, Bs)) + C > 0:
            ans += 1
    return ans


if __name__ == "__main__":
    N, M, C = tuple(map(int, input().split(" ")))
    Bs = list(tuple(map(int, input().split(" "))))
    As = list(list(tuple(map(int, input().split(" ")))) for __ in range(N))
    print(solve(N, M, C, Bs, As))
