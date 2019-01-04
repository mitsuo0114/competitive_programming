from collections import defaultdict, deque
#
# def fast_solve(As):
#     As = sorted(As)
#     Ns = []
#     for a in As:
#         if len(Ns) < 2:
#             Ns.append(a)
#         else:
#             imax = 0
#             nimax = 0
#             for ni in range(len(Ns) + 1):
#                 new_right = abs(a - Ns[ni]) if ni != len(Ns) else 0
#                 new_left = abs(Ns[ni - 1] - a) if ni != 0 else 0
#                 original = 0
#                 if 0 < ni < len(Ns) - 1:
#                     original = abs(Ns[ni + 1] - Ns[ni])
#                 m = new_left + new_right - original
#                 if m > imax:
#                     nimax = ni
#                     imax = m
#             Ns.insert(nimax, a)
#     print(Ns)
#     N = len(Ns)
#     print( sum([abs(Ns[i + 1] - Ns[i]) for i in range(N - 1)]))

# N = int(input())
# As = [int(input()) for _ in range(N)]

def slow_solve(As):
    from itertools import permutations
    nmax = 0
    N = len(As)
    for Ns in permutations(As, len(As)):
        m = sum([abs(Ns[i + 1] - Ns[i]) for i in range(N - 1)])
        nmax = max(m, nmax)
    return nmax

def fast_solve(As):
    As = sorted(As)
    N = len(As)
    h = N // 2
    # if N % 2 == 1:
    #     h += 1
    return As[h+1] + As[h] + sum(As[h + 2:]) * 2 - sum(As[:h]) * 2

# print(slow_solve(As))
#
#
# #
# # def fast_solve(As):
# #     if len(As) <= 2:
# #         return 0
# #     if len(As) == 3:
# #         return max(abs(As[0] - As[1]) + abs(As[1] - As[2]),
# #                    abs(As[0] - As[2]) + abs(As[2] - As[1]),
# #                    abs(As[1] - As[0]) + abs(As[0] - As[2]))
# #     else:
# #         m = 0
# #         for i in range(len(As) - 1):
# #             c = fast_solve(As[0:i]) + fast_solve(As[i+1:]) + abs(As[i] - As[i+1])
# #             m = max(c, m)
# #         return m
#
#
#
#
# def Ford_Fulkerson(s):
#     start = -1
#     end = -2
#     V1 = As[::]
#     V2 = As[::]
#     N = len(As)
#     lines = defaultdict(set)
#     cost = [[0] * N for i in range(N)]
#     for i1, v1 in enumerate(V1):
#         lines[start].add(i1)
#         lines[i1 + N].add(end)
#         for i2, v2 in enumerate(V2):
#             if i1 != i2:
#                 lines[i1].add(i2 + N)
#                 cost[i1][i2 + N] = abs(v1 - v2)
#     # BFS用のdeque
#     queue = deque()
#     queue.append([s, 10**10])
#     # 到達済み判定用
#     ed = [True] * N
#     ed[s] = False
#     # ルート
#     route = [0 for i in range(N)]
#     route[s] = -1
#     while queue:
#         s, flow = queue.pop()
#         for t in lines[s]:  # s->t
#             if ed[t]:  # 未到達
#                 flow = min(cost[s][t], flow)  # flow = min(直前のflow,その辺のコスト)
#                 route[t] = s
#                 queue.append([t, flow])
#                 ed[t] = False
#                 if t == end:  # ゴール到達
#                     ans += flow
#                     break
#         else:
#             continue  # breakされなければWhile節の先頭に戻る
#         break
#     else:
#         return False
#
# def fast_solve(As):
#     while True:
#         if Ford_Fulkerson(As):
#             continue
#         else:
#             break
#     print(ans)
#
print(fast_solve([6,
                  8,
                  1,
                  2,
                  3]))
#
