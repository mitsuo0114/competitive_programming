import string


def solve(S):
    ans = 1000
    for v in string.ascii_lowercase:
        tans = 0
        s = S
        while s.count(v) < len(s):
            tans += 1
            ns = []
            for i in range(len(s) - 1):
                if s[i] == v or s[i + 1] == v:
                    ns.append(v)
                else:
                    ns.append(s[i])
            s = "".join(ns)
        ans = min(ans, tans)

    return ans


assert (solve("serval") == 3)
assert (solve("jackal") == 2)
assert (solve("zzz") == 0)
assert (solve("whbrjpjyhsrywlqjxdbrbaomnw") == 8)

if __name__ == "__main__":
    print(solve(input()))
