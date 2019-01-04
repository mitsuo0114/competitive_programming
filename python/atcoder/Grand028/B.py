import random
from collections import Counter
from itertools import combinations

def ans_solve(N, As):
    C = Counter(As)
    ans = 0
    for d in reversed(sorted(As)):
        n = (2 ** d.bit_length()) - d
        if d != n:
            if C[d] > 0 and C.get(n, 0) > 0:
                C[d] -= 1
                C[n] -= 1
                ans += 1
        else:
            ans += C[d]//2
            C[d] = 0
    return ans


print(ans_solve(5, [3, 11, 14, 5, 13]))


def solve(N, As):
    data = {}
    for i, a in enumerate(As):
        data.setdefault(a, []).append(i)
    d_pairs = []
    counters = Counter()
    keys = list(sorted(data.keys()))
    for v in combinations(keys, 2):
        if bin(v[0] + v[1]).count("1") == 1:
            d_pairs.append((v[0], v[1]))
            counters.update([v[0]] * len(data[v[0]]))
            counters.update([v[1]] * len(data[v[1]]))
    for v in keys:
        if bin(v * 2).count("1") == 1:
            d_pairs.append((v, v))
            counters.update([v] * len(data[v]))
    cost = []
    for p in d_pairs:
        c1 = counters[p[0]] if bin(p[0]).count("1") != 1 else 10 ** 10
        c2 = counters[p[1]] if bin(p[1]).count("1") != 1 else 10 ** 10
        cost.append((c1 + c2, p[0], p[1]))

    ans = 0
    cost.sort()
    for cost_pair in cost:
        if cost_pair[1] != cost_pair[2]:
            while len(data[cost_pair[1]]) > 0 and len(data[cost_pair[2]]) > 0:
                ans += 1
                data[cost_pair[1]].pop()
                data[cost_pair[2]].pop()
        else:
            while len(data[cost_pair[1]]) > 1:
                ans += 1
                data[cost_pair[1]].pop()
                data[cost_pair[2]].pop()
    return ans
#
#
# def slow_solve(N, As):
#     As.sort()
#     pairs = []
#     counter = Counter()
#     for i, a in enumerate(As):
#         for j, aa in enumerate(As[i + 1:]):
#             if bin(a + aa).count("1") == 1:
#                 pairs.append((i, j + i + 1))
#                 counter.update([i, j + i + 1])
#     cost = []
#     for p in pairs:
#         if p[0] != p[1]:
#             cost.append((min(counter[p[0]], counter[p[1]]), p[0], p[1]))
#         else:
#             cost.append((10 ** 10, p[0], p[1]))
#     used = set()
#     ans = 0
#     for cost_pair in sorted(cost):
#         if cost_pair[1] not in used and cost_pair[2] not in used:
#             ans += 1
#             used.add(cost_pair[1])
#             used.add(cost_pair[2])
#     return ans

#
# # # print(solve(5, [3, 11, 14, 5, 13]))
import random
#
for i in range(10):
    r = [random.randint(1, 10*9) for _ in range(20000)]
    print("s")
#     ans_solve(5, r)
    # if  == solve(5, r):
    #     print(i)
    # else:
    #     print("out : ", r)
    #     print(ans_solve(5, r))
    #     print(solve(5, r))
    #     break
# #
print(ans_solve(10, [2, 2, 4, 5, 6, 7, 8, 9, 10, 10]))
print((ans_solve(10, [2, 2, 4, 5, 6, 7, 8, 9, 10, 10]) == solve(10, [2, 2, 4, 5, 6, 7, 8, 9, 10, 10])))
print((ans_solve(10, [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == solve(10, [1, 1, 2, 2, 2, 2, 3, 3, 3, 3])))
print((ans_solve(3, [1, 2, 3]) == solve(3, [1, 2, 3])))
print((ans_solve(5, [3, 11, 14, 5, 13]) == solve(5, [3, 11, 14, 5, 13])))
print((ans_solve(5, [1] * 100) == solve(5, [1] * 100)))
print((ans_solve(5, [2] * 1000) == 500))
print((ans_solve(5, [1] * 20000) == 10000))
# # # print((slow_solve(5, [1] * 100) == 50))
# # # # print((slow_solve(5, [1] * 1000) == 500))
# # # # print((slow_solve(5, [2] * 1000) == 500))
# print((solve(5, [1] * 10000) == 5000))


if __name__ == "__main__":
    N = input()
    As = [int(c) for c in input().split()]
    print(ans_solve(N, As))
