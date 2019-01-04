


def solve(N, K, As):
    alls = []
    for i in range(N):
        for j in range(i + 1, N + 1):
            alls.append("{:061b}".format(sum(As[i:j])))
    def find(i, alls):
        if i > 60:
            return []
        ones = [a for a in alls if a[i] == "1"]
        if len(ones) < K:
            return find(i + 1, alls)
        elif len(ones) == K:
            return ones
        elif len(ones) > K:
            ret = find(i + 1, ones)
            if len(ret) == 0:
                return ones[0:K]
            else:
                return ret

    ans = find(0, alls)
    if len(ans):
        a = 0xFFFFFFFFFFF
        for p in ans:
            a &= int(p, 2)
        return a
    else:
        return 0
#
# import random
# from itertools import combinations
#
#
# def slow_solve(N, K, As):
#     alls = []
#     for i in range(N):
#         for j in range(i + 1, N + 1):
#             alls.append(sum(As[i:j]))
#     m = 0
#     for c in combinations(alls, K):
#         a = 0xFFFFFFFFFFF
#         for p in c:
#             a &= p
#         m = max(m, a)
#     return m
# # print(solve(4, 2, [2, 5, 2, 5]))
# # print(solve(8, 4, [9, 1, 8, 2, 7, 5, 6, 4]))
# # print(slow_solve(7, 1, [531782269, 766602361, 332603064, 967430212, 158074762, 798196507, 778150211]))
# # print(solve(7, 1, [531782269, 766602361, 332603064, 967430212, 158074762, 798196507, 778150211]))
# # import random
# #
# # while 1:
# #     N = []
# #     for n in range(0, 10):
# #         N.append(random.randint(1, 10**9+1))
# #         # for k in range(1, (len(N) * (len(N) + 1) // 2) + 1):
# #         for k in range(1, 3):
# #             if slow_solve(len(N), k, N) == solve(len(N), k, N):
# #                 print("ok", len(N), k, N)
# #             else:
# #                 print("ng########")
# #                 print("slow : ", slow_solve(len(N), k, N))
# #                 print("solve : ", solve(len(N), k, N))
# #                 print(N, k)


if __name__ == "__main__":
    l = input()
    N = int(l.split(" ")[0])
    K = int(l.split(" ")[1])
    As = [int(c) for c in input().split()]
    print(solve(N, K, As))
