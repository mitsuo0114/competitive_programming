def solve(A, B, C):
    A, B, C = max(A, B, C), sum([A, B, C]) - max(A, B, C) - min(A, B, C), min(A, B, C)
    if A % 2 == B % 2 == C % 2:
        ans = 0
    else:
        ans = 1
        if B % 2 == C % 2:
            B += 1
            C += 1
        elif A % 2 == B % 2:
            A += 1
            B += 1
        else:
            A += 1
            C += 1
    ans += (A - B) // 2 + (A - C) // 2
    return ans


assert (solve(0, 0, 0) == 0)
assert (solve(1, 0, 0) == 1)
assert (solve(1, 1, 0) == 2)
assert (solve(1, 0, 1) == 2)
assert (solve(1, 1, 1) == 0)

assert (solve(2, 0, 0) == 2)
assert (solve(2, 2, 0) == 1)
assert (solve(2, 0, 2) == 1)
assert (solve(2, 2, 2) == 0)

assert (solve(2, 1, 0) == 3)
assert (solve(2, 2, 1) == 2)
assert (solve(2, 1, 2) == 2)
assert (solve(3, 2, 2) == 1)

if __name__ == "__main__":
    A, B, C = tuple(map(int, input().split(" ")))
    print(solve(A, B, C))
