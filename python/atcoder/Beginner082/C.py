from collections import Counter


def solve(N, As):
    c = Counter(As)
    ans = 0
    for k, v in c.items():
        if k < v:
            ans += v - k
        elif k == v:
            pass
        else:
            ans += v
    return ans

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
