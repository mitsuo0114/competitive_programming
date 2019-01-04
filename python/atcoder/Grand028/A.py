# def slow_solve(S):
#     if len(S) == 1:
#         return 0
#
#     ans = 0
#     while "BW" in S:
#         S = list(S)
#         for i in range(0, len(S) - 1):
#             if S[i] == "B" and S[i + 1] == "W":
#                 ans += 1
#                 S[i] = "W"
#                 S[i+1] = "B"
#         S = "".join(S)
#         print(S)
#     return ans
#
# print(solve("BBW"))
# print(solve("BWBWBW"))
# print(slow_solve("BBBWWW") == solve("BBBWWW"))
# print(slow_solve("BBWBWW") == solve("BBWBWW"))
# print(solve("BW" * 5000))
# print(slow_solve("BBWBWW") == 8)
# print(slow_solve("BW" * 5000) == 6)


def solve(S):
    if len(S) == 1:
        return 0

    j = 0
    ans = 0
    for i in range(0, len(S)):
        if S[i] == "W":
            ans += (i - j)
            j += 1
    return ans


if __name__ == "__main__":
    print(solve(input()))
