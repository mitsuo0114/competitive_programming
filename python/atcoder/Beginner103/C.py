def solve(N, As):
    return sum([a - 1 for a in As])


assert (solve(1, [2]) == 1)
assert (solve(2, [2, 3]) == 3)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
