import string
chars = string.ascii_lowercase
def solve(S):
    for c in chars:
        if c not in S:
            return S + c

    S = S[::-1]
    for i, c in enumerate(S):
        if i == len(S) - 1:
            return -1

        c = S[i + 1]
        if c == chars[-1]:
            continue

        ans = S[i + 2:]
        n = chars[chars.find(c) + 1]
        while n in ans:
            if n == chars[-1]:
                n = -1
                break
            n = chars[chars.find(n)+1]
        if n == -1:
            continue
        ans = ans[::-1]
        ans += n
        return ans



chars = "abc"
assert (solve("a") == "ab")
assert (solve("ab") == "abc")
assert (solve("abc") == "ac")
assert (solve("ac") == "acb")
assert (solve("acb") == "b")
assert (solve("b") == "ba")
assert (solve("ba") == "bac")
assert (solve("bac") == "bc")
assert (solve("bc") == "bca")
assert (solve("bca") == "c")
assert (solve("c") == "ca")
assert (solve("ca") == "cab")
assert (solve("cab") == "cb")
assert (solve("cb") == "cba")
assert (solve("cba") == -1)

chars = "abcd"
assert (solve("dbac") == "dbc")

chars = string.ascii_lowercase
assert (solve("yxwvutsrqponmlkjihgfedcba") == "yxwvutsrqponmlkjihgfedcbaz")
# assert (solve("yxwvutsrqponmlkjihgfedcbza") == "z")
assert (solve("yxwvutsrqponmlkjihgfedcbaz") == "yxwvutsrqponmlkjihgfedcbz")

assert (solve("zyxwvutsrqponmlkjihgfedcb") == "zyxwvutsrqponmlkjihgfedcba")
assert (solve("zyxwvutsrqponmlkjihgfedca") == "zyxwvutsrqponmlkjihgfedcab")
assert (solve("zyxwvutsrqponmlkjihgfedcab") == "zyxwvutsrqponmlkjihgfedcb")
assert (solve("zyxwvutsrqponmlkjihgfedcb") == "zyxwvutsrqponmlkjihgfedcba")
assert (solve("zyxwvutsrqponmlkjihgfedcba") == -1)
assert (solve("atcoder") == "atcoderb")
assert (solve("abcdefghijklmnopqrstuvwzyx") == "abcdefghijklmnopqrstuvx")

if __name__ == "__main__":
    print(solve(input()))
