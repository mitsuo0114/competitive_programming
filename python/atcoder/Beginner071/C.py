from collections import Counter


def solve(N, As):
    c = Counter(As)
    two = sorted([i for i, v in c.items() if v >= 2])
    four = [i for i, v in c.items() if v >= 4]
    ans = 0
    if len(two) >= 2:
        ans = two[-1] * two[-2]
    if len(four):
        ans = max(max(four) * max(four), ans)
    return ans


assert (solve(4, [1, 1, 2, 2]) == 2)
assert (solve(4, [2, 2, 2, 2]) == 4)
assert (solve(4, [2, 2, 3, 3]) == 6)

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
