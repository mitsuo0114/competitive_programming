from collections import Counter


def solve(N, As):
    counter = Counter(As)
    if len(counter) % 2 == 0:
        return len(counter) - 1
    return len(counter)


assert (solve(5, [1, 2, 1, 3, 7]) == 3)
assert (solve(15, [1, 3, 5, 2, 1, 3, 2, 8, 8, 6, 2, 6, 11, 1, 1]) == 7)
print("OK")

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
