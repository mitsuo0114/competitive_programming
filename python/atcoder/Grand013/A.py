def solve(N, As):
    increasing = None
    ans = 1
    for a1, a2 in zip(As, As[1:]):
        if increasing is None:
            if a1 < a2:
                increasing = True
            elif a1 > a2:
                increasing = False
        else:
            if a1 == a2 or (a1 < a2 and increasing) or (a1 > a2 and not increasing):
                pass
            else:
                ans += 1
                increasing = None
    return ans


assert (solve(1, [1, 2]) == 1)
assert (solve(1, [1, 2, 1, 2]) == 2)
assert (solve(1, [2, 1]) == 1)
assert (solve(1, [1, 2, 3]) == 1)
assert (solve(1, [1, 2, 3, 2]) == 2)
assert (solve(1, [1, 2, 3, 2, 1]) == 2)
assert (solve(1, [3, 2, 1]) == 1)
assert (solve(1, [3, 2, 3]) == 2)
assert (solve(1, [1, 2, 1]) == 2)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
