def solve(L, As):
    print(L, ",", As)
    Ams = [a % 2 for a in As]
    # ans = 10 ** 15
    # for i in range(L):
    #     ans = min(ans,
    #               sum([1 for a in Ams[:i] if a % 2 == 0]) + sum([1 for a in Ams[i:] if a % 2 == 1]),
    #               sum([1 for a in Ams[:i] if a % 2 == 1]) + sum([1 for a in Ams[i:] if a % 2 == 0]))
    ans = 0
    for i in range(L - 1):
        if Ams[i] != Ams[i + 1]:
            ans += 1
    return max(ans - 1, 0)


assert (solve(3, [1, 1, 1]) == 0)
assert (solve(3, [1, 1, 2]) == 0)
assert (solve(3, [2, 1, 1]) == 0)
assert (solve(3, [2, 2, 1]) == 0)
assert (solve(3, [1, 2, 2]) == 0)
assert (solve(3, [2, 2, 2]) == 0)
assert (solve(3, [1, 1, 3]) == 0)
assert (solve(3, [3, 1, 3]) == 0)
assert (solve(3, [2, 1, 3]) == 0)
assert (solve(3, [1, 1, 0]) == 0)
assert (solve(3, [1, 2, 3]) == 1)
assert (solve(4, [1, 0, 2, 3]) == 1)
assert (solve(4, [1, 0, 1, 2]) == 1)
assert (solve(8 , [2, 0, 0, 2, 1, 3, 4, 1]) == 3)
assert (solve(7, [314159265, 358979323, 846264338, 327950288, 419716939, 937510582, 0]) == 1)

if __name__ == "__main__":
    L = int(input())
    As = [int(input()) for _ in range(L)]
    print(solve(L, As))

