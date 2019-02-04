from collections import Counter
import string


def solve(N, Ss):
    counters = []
    for s in Ss:
        counters.append(Counter(s))
    ans = ""
    for c in string.ascii_lowercase:
        vs = [counter[c] for counter in counters if c in counter]
        if len(vs) == N:
            ans += c * min(vs)
    return ans


# assert (solve(1, ["abc"]) == "abc")
# assert (solve(2, ["abc", "ab"]) == "ab")
# assert (solve(2, ["abc", "ab"]) == "ab")

if __name__ == "__main__":
    n = int(input())
    Ss = [input() for _ in range(n)]
    print(solve(n, Ss))
