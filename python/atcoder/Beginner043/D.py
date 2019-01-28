def solve(s):
    for i, j in zip(range(0, len(s) - 1), range(1, len(s))):
        if s[i] == s[j]:
            return "%d %d" % (i + 1, j + 1)

    for i, j in zip(range(0, len(s) - 2), range(2, len(s))):
        if s[i] == s[j]:
            return "%d %d" % (i + 1, j + 1)

    return "%d %d" % (-1, -1)

assert (solve("ee") == "1 2")
assert (solve("eeded") == "1 2")
assert (solve("abcdd") == "4 5")
assert (solve("needed") == "2 3")
assert (solve("atcoder") == "-1 -1")
assert (solve("abaca") == "1 3")
assert (solve("cbaca") == "3 5")
assert (solve("abc" * 5000) == "-1 -1")

if __name__ == "__main__":
    print(solve(input()))
