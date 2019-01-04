# for n in range(N):
#     ni = int(L / N * n)
#     X[ni] = S[n]
#
# for m in range(M):
#     mi = int(L / M * m)
#     X[mi] = T[m]
# Ns = [S[int(L / N * n)] for n in range(N)]
# Ms = [T[int(L / M * m)] for m in range(M) if int(L / M * m) < M]
# # D = set(Ns).intersection(set(Ms))
# print( Ns, Ms, S, T)
# for d in D:
#     if d < N and d < M and S[d] != T[d]:
#         return -1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solve(N, M, S, T):
    L = N * M // gcd(N, M)
    X = ["Z" for _ in range(L)]
    for k in range(L):
        ni = int(L / N * k)
        mi = int(L / M * k)
        if k < N:
            if X[ni] != "Z" and X[ni] != S[k]:
                return -1
            else:
                X[ni] = S[k]
        if k < M:
            if X[mi] != "Z" and X[mi] != T[k]:
                return -1
            else:
                X[mi] = T[k]

    return "".join(X).lower()


if __name__ == "__main__":
    # l = input()
    # N, M = int(l.split()[0]),int(l.split()[1])
    # S = input()
    # T = input()
    # print(solve(N, M, S, T))
    # print(solve(1, 1, "a", "a"))
    # print(solve(2, 2, "ab", "ba"))
    # print(solve(3, 2, "acp", "ae"))
    # print(solve(6, 3, "abcdef", "abc"))
    # print(solve(15, 9, "dnsusrayukuaiia", "dujrunuma"))
    print(solve(3, 5, "aaa", "abbbb"))
    print(solve(1, 2, "a", "ab"))
    print(solve(2, 4, "aa", "abab"))
    print(solve(2, 4, "ab", "abbb"))

import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(3, 70, [20, 30, 10]), 2)

    def test_2(self):
        self.assertEqual(solve(3, 10, [20, 30, 10]), 1)

    def test_3(self):
        self.assertEqual(solve(4, 1111, [1, 10, 100, 1000]), 4)

    def test_4(self):
        self.assertEqual(solve(2, 10, [20, 20]), 0)
