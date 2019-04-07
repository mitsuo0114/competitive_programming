# def solve(N, P):
#     stack = []
#     ans = []
#     E_count = 0
#     S_count = 0
#
#     direction = False
#     for p in P:
#         E_count = E_count + 1 if p == "E" else E_count
#         S_count = S_count + 1 if p == "S" else S_count
#
#         if E_count == N - 1:
#             print(ans)
#             ans += ["S"] * (N - 1 - ans.count("S"))
#             ans += ["E"] * (N - 1 - ans.count("E"))
#             break
#
#         if S_count == N - 1:
#             print(ans)
#             ans += ["E"] * (N - 1 - ans.count("E"))
#             ans += ["S"] * (N - 1 - ans.count("S"))
#             break
#
#         if len(stack) == 0:
#             stack.append(p)
#             direction = p
#         elif direction == p:
#             stack.append(p)
#         else:
#             stack.append(p)
#             ans.extend(stack[::-1])
#             stack = []
#             print(ans)
#
#     print(ans)
#     return "".join(ans)


def solve(N, P):
    if P[0] != P[-1]:
        return P[-1] * (N - 1) + P[0] * (N - 1)
    else:
        t = "E" if P[0] == "S" else "S"
        c = 0
        for i in range(len(P)):
            if P[i] == t:
                c += 1
            if P[i] == t and P[i + 1] == t:
                break

        return c * t + P[0] * (N - 1) + t * (N - 1 - c)


assert (solve(2, "SE") == "ES")
assert (solve(5, "SSSSEEEE") == "EEEESSSS")
assert (solve(5, "EEEESSSS") == "SSSSEEEE")
assert (solve(5, "EESSSESE") == "SEEEESSS")
assert (solve(5, "SEEESSES") == "ESSSSEEE")
assert (solve(5, "SESESEES") == "EEESSSSE")
assert (solve(3, "SSEE") == "EESS")
assert (solve(3, "SEES") == "ESSE")
assert (solve(3, "ESSE") == "SEES")
# assert (solve(5, "EESSSESE") == "SEEEESSS")

k = 50000
assert (solve(k, "ES" * (k - 1)) == "S" * (k - 1) + "E" * (k - 1))
assert (solve(k, "E" * (k - 1) + "S" * (k - 1)) == "S" * (k - 1) + "E" * (k - 1))

t = int(input())
for case in range(1, t + 1):
    N = int(input())
    l = input()
    print("Case #%d: %s" % (case, solve(N, l)))
