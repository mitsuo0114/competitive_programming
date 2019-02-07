from collections import Counter


def solve(N, S):
    c = Counter(S)
    ans = 3 * 10 ** 5 + 1

    right_e = c["E"]
    left_w = 0
    for i in range(N):
        if S[i] == "E":
            right_e -= 1

        ans = min(ans, left_w + right_e)

        if S[i] == "W":
            left_w += 1
    return ans


assert (solve(2, "EW") == 0)
assert (solve(2, "WE") == 1)
assert (solve(2, "WW") == 0)
assert (solve(2, "EE") == 0)
assert (solve(3, "EEW") == 0)
assert (solve(3, "EEE") == 0)

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))
