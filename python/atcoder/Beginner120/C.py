def solve(S):
    return min(S.count("1"), S.count("0")) * 2

    ans = 0
    i = 0
    j = 1
    taken = [1 for _ in S]
    while j < len(S):
        if S[i] != S[j]:
            taken[i] = 0
            taken[j] = 0
            ans += 2

            j += 1
            while taken[i] == 0:
                i -= 1
                if i == -1:
                    i = j
                    j = j + 1
                if j >= len(S):
                    break
        else:
            i += 1
            j += 1

    return ans

assert (solve("1") == 0)
assert (solve("0") == 0)
assert (solve("10") == 2)
assert (solve("101") == 2)
assert (solve("100") == 2)
assert (solve("01") == 2)
assert (solve("011") == 2)
assert (solve("0110") == 4)
assert (solve("1100") == 4)
assert (solve("111000") == 6)
assert (solve("101010") == 6)
assert (solve("000000") == 0)
assert (solve("010000") == 2)
assert (solve("011000") == 4)
assert (solve("011010") == 6)
assert (solve("011110") == 4)
assert (solve("000011110000") == 8)
assert (solve("101110") == 4)
assert (solve("100010") == 4)
assert (solve("010") == 2)
assert (solve("0" * 10000) == 0)
assert (solve("1" * 10000) == 0)
assert (solve("1" * 5000 + "0" * 1) == 2)
assert (solve("10" * 5000) == 10000)

if __name__ == "__main__":
    S = input()
    print(solve(S))
