

def solve(N, K, tds):
    tds.sort(reverse=True, key=lambda x: x[1])

    has = tds[:K]
    v = {t[0]: 0 for t in tds}
    for t in has:
        v[t[0]] += 1
    has.sort(key=lambda x: x[1])

    nothas = tds[K:]
    nothas.sort(reverse=True, key=lambda x: x[1])

    tmp_max = sum(t[1] for t in tds[:K])
    various = len(set([t[0] for t in tds[:K]]))
    mm = tmp_max + various ** 2
    for _ in range(0, N):
        target = None
        for i, t in enumerate(has):
            if v[t[0]] > 1:
                v[t[0]] -= 1
                tmp_max -= t[1]
                target = i
                break
        if target is not None:
            del has[target]
        else:
            break

        target = None
        for i, t in enumerate(nothas):
            if v[t[0]] == 0:
                v[t[0]] += 1
                tmp_max += t[1]
                target = i
                break
        if target is not None:
            del nothas[target]
        else:
            break

        various += 1
        mm = max(mm, tmp_max + various ** 2)

    return mm


# def solve(N, K, tds):
#     memos = {}
#     tds.sort()
#
#     def dfs(n, k, ee, neta_count):
#         if (n, k, ee, neta_count) in memos:
#             return memos[(n, k, ee, neta_count)]
#
#         if n == N or k == 0:
#             memos[(n, k, ee, neta_count)] = neta_count * neta_count
#             return memos[(n, k, ee, neta_count)]
#
#         if ee == tds[n][0]:
#             eaten = dfs(n + 1, k - 1, tds[n][0], neta_count) + tds[n][1]
#         else:
#             eaten = dfs(n + 1, k - 1, tds[n][0], neta_count + 1) + tds[n][1]
#
#         uneaten = dfs(n + 1, k, ee, neta_count)
#
#         memos[(n, k, ee, neta_count)] = max(eaten, uneaten)
#         return memos[(n, k, ee, neta_count)]
#
#     return dfs(0, K, -1, 0)

assert (solve(1, 1, [(1, 9)]) == 9 + 1)
assert (solve(2, 1, [(1, 9), (2, 10)]) == 10 + 1)
assert (solve(2, 1, [(1, 9), (1, 10)]) == 10 + 1)
assert (solve(2, 2, [(1, 9), (2, 10)]) == 19 + 2 * 2)
assert (solve(5, 3, [(1, 9), (1, 7), (2, 6), (2, 5), (3, 1)]) == 26)
assert (solve(3, 2, [(1, 1), (1, 2), (1, 3)]) == 5 + 1)
assert (solve(3, 2, [(2, 1), (1, 2), (1, 3)]) == 4 + 4)
assert (solve(3, 2, [(1, 1), (2, 1), (3, 1)]) == 2 + 4)
assert (solve(4, 3, [(1, 1), (2, 1), (3, 1), (4, 1)]) == 3 + 9)
assert (solve(5, 3, [(1, 1), (2, 1), (3, 1), (4, 1), (4, 1)]) == 3 + 9)
assert (solve(10000, 10000, [(i, 10 ** 9) for i in range(1, 10001)]) == 10 ** 9 * 10000 + 10000 * 10000)
print("OK")

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    tds = [tuple(map(int, input().split(" "))) for _ in range(N)]
    print(solve(N, K, tds))
