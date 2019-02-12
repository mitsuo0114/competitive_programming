def solve(N, As):
    As.sort()
    return sum([n for n in As[N::2]])
    # return max(
    #     sum([n for n in As[N:N * 2]]),
    #     sum([n for n in As[1::3]]),
    #     sum([n for n in As[N+2::2]]))


assert (solve(1, [1, 2, 2]) == 2)
assert (solve(1, [3, 3, 3]) == 3)
assert (solve(2, [5, 2, 8, 5, 1, 5]) == 10)
assert (solve(10, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000,
                   1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000,
                   1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000,
                   1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
              ) == 10000000000
        )
if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
