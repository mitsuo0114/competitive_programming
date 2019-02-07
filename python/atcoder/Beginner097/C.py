import string


def solve(s, K):
    candidate = set()
    for char in string.ascii_lowercase:
        for i, c in enumerate(s):
            if c == char:
                for j in range(i + 1, min(len(s), i + 5) + 1):
                    candidate.add(s[i:j])
        if len(candidate) >= K:
            break
    return sorted(list(candidate))[K - 1]


assert (solve("aba", 4) == "b")
assert (solve("atcoderandatcodeer", 5) == "andat")
assert (solve("z", 1) == "z")
assert (solve("a", 1) == "a")
assert (solve("aa", 2) == "aa")
assert (solve("aaa", 3) == "aaa")
assert (solve("aaaa", 4) == "aaaa")
assert (solve("aaaaa", 5) == "aaaaa")
assert (solve("aaaaa", 4) == "aaaa")

if __name__ == "__main__":
    s = input()
    K = int(input())
    print(solve(s, K))
