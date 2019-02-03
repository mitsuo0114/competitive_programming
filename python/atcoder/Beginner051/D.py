# GIVE UP,,,,,
#
# import heapq
#
#
# def dist(N, a, b, w_mat):
#     ds = [10 ** 10 for _ in range(N + 1)]
#     q = [(0, a)]
#     ds[a] = 0
#     heapq.heapify(q)
#     # print("\n".join([str(r) for r in w_mat]))
#     while len(q):
#         # print(q)
#         # print(a, b, ds[1:])
#         w, i = heapq.heappop(q)
#         if i == b:
#             break
#         for ni, wi in [(ni, wi) for ni, wi in enumerate(w_mat[i]) if wi > 0]:
#             if ds[ni] > w + wi:
#                 ds[ni] = w + wi
#                 heapq.heappush(q, (w + wi, ni))
#     # print("\n".join([str(r) for r in d_mat]))
#     # print(a, b, ds[1:])
#     return ds[b]
#
#
# def solve(N, M, ABCs):
#     # print(N, ",", M, ",", ABCs)
#     d_mat = [[0 for __ in range(N + 1)] for _ in range(N + 1)]
#     w_mat = [[-1 for __ in range(N + 1)] for _ in range(N + 1)]
#
#     for i in range(N + 1):
#         w_mat[i][i] = 0
#
#     for a, b, c in ABCs:
#         w_mat[a][b] = c
#         w_mat[b][a] = c
#
#     for s in range(1, N + 1):
#         for e in range(s + 1, N + 1):
#             d = dist(N, s, e, w_mat)
#             d_mat[s][e] = d
#             d_mat[e][s] = d
#
#     ans = 0
#     for a, b, c in ABCs:
#         if all(d_mat[s][e] != d_mat[s][a] + c + d_mat[b][e]
#                for s in range(1, N + 1)
#                for e in range(s + 1, N + 1)):
#             ans += 1
#
#     #    print("\n".join([str(r) for r in d_mat]))
#     return ans
#
#
# assert (solve(3, 3, [(1, 2, 1), (1, 3, 1), (2, 3, 3)]) == 1)
# assert (solve(3, 2, [(1, 2, 1), (2, 3, 1)]) == 0)
#
# if __name__ == "__main__":
#     N, M = tuple(map(int, input().split(" ")))
#     ABCs = [tuple(map(int, input().split(" "))) for _ in range(M)]
#     print(solve(N, M, ABCs))
