def solve(A, B, C):
    ans = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        ans += 1
        pA, pB, pC = A, B, C
        A, B, C = B // 2 + C // 2, A // 2 + C // 2, A // 2 + B // 2
        if pA == A and pB == B and pC == C:
            return -1
    return ans


assert (solve(2, 4, 8) == 1)
assert (solve(4, 4, 8) == 2)
assert (solve(4, 8, 8) == 2)
assert (solve(16, 8, 8) == 3)
assert (solve(4, 12, 20) == 3)
assert (solve(14, 14, 14) == -1)
assert (solve(454, 414, 444) == 1)

if __name__ == "__main__":
    A, B, C = tuple(map(int, input().split(" ")))
    print(solve(A, B, C))
