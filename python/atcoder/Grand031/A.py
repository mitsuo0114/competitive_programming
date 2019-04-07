from collections import Counter
def solve(N, S):
    d = 10**9 + 7
    c = Counter(S)
    ans = 1
    for ch, count in c.items():
        ans *= (count + 1)
    ans %= d
    return ans - 1

assert(solve(1, "a") == 1)
assert(solve(2, "ab") == 3)
assert(solve(3, "abc") == 7)
assert(solve(3, "baa") == 5)
assert(solve(6, "abcab") == 17)
# assert(solve(5, 2, 9) == 10)
# assert(solve(8, 8, 1) == 9)
# assert(solve(0, 100, 0) == 100)

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))
