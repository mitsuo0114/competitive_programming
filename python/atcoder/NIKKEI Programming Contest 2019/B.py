def solve(N, A, B, C):
    ans = 0
    for a, b, c in zip(A, B, C):
        if a == b and b == c and a == c:
            pass
        elif a == b or b == c or a == c:
            ans += 1
        else:
            ans += 2
    return ans


if __name__ == "__main__":
    N = int(input())
    A = input()
    B = input()
    C = input()
    print(solve(N, A, B, C))
