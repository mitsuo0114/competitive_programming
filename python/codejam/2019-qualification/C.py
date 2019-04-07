import string
import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


assert (gcd(3, 5) == 1)
assert (gcd(4, 2) == 2)
assert (gcd(2, 2) == 2)
assert (gcd(100, 50) == 50)
assert (gcd(11 * 13, 11 * 13 * 17) == 11 * 13)


def solve(N, L, S):
    Gs = []
    for i in range(L - 1):
        if S[i] != S[i + 1]:
            g = gcd(S[i], S[i + 1])
            Gs.append(g)

    Gs = list(set(Gs))
    while len(Gs) != len(string.ascii_uppercase):
        for s in S:
            for g in Gs:
                c = s // g
                if s % g == 0 and c not in Gs:
                    Gs.append(c)
        Gs = list(set(Gs))

    dec_table = {g: c for c, g in zip(string.ascii_uppercase, sorted(Gs))}

    def find_first(S, table):
        s = S[0]
        for t in table:
            if s % t == 0:
                a, b = t, s // t
                break
        i = 0
        while S[i] == s:
            i += 1
        if S[i] % a == 0:
            i += 1
        if i % 2 == 0:
            return b
        else:
            return a

    index = find_first(S, dec_table)
    ans = [dec_table[index]]
    for s in S:
        index = s // index
        ans.append(dec_table[index])

    return "".join(ans)


def gen_map():
    def is_prime(n):
        m = int(math.sqrt(n))
        for k in range(2, m + 1):
            if n % k == 0:
                return False
        return True

    import random

    m = set()
    m.add(2)
    while True:
        b = random.randint(2, 1000)
        if is_prime(b) and b not in m:
            m.add(b)
            if len(m) == len(string.ascii_uppercase):
                dec_table = {}
                for c, g in zip(string.ascii_uppercase, sorted(list(m))):
                    dec_table[c] = g
                return dec_table


def encrypt(str, m):
    ret = []
    for i in range(len(str) - 1):
        ret.append(m[str[i]] * m[str[i + 1]])
    return ret


import random

for _ in range(0, 10000):
    m = gen_map()
    str = string.ascii_uppercase * 10 + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    str = [c for c in str]
    random.shuffle(str)
    str = "".join(str)
    print(str)
    encrypted = encrypt(str, m)
    assert (solve(0, len(str) - 1, encrypted) == str)

assert (solve(103, 31,
              [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697,
               3239,
               7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]) == "CJQUIZKNOWBEVYOFDPFLUXALGORITHMS")

assert (solve(10000, 25,
              [3292937, 175597, 18779, 50429, 375469, 1651121, 2102, 3722, 2376497, 611683, 489059, 2328901, 3150061,
               829981, 421301, 76409, 38477, 291931, 730241, 959821, 1664197, 3057407, 4267589, 4729181, 5335543
               ]) == "SUBDERMATOGLYPHICFJKNQVWXZ")

assert (solve(103, 32,
              [49, 217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003,
               697,
               3239,
               7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]) == "CCJQUIZKNOWBEVYOFDPFLUXALGORITHMS")

print("OK")

t = int(input())
for case in range(1, t + 1):
    N, L = tuple(map(int, input().split(" ")))
    S = list(map(int, input().split(" ")))
    print("Case #%d: %s" % (case, solve(N, L, S)))
