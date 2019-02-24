def solve(N, S):
    k = 0
    ans = 0

    for c in S:
        k = 0 if c == "B" else k + 1
        ans += k

    if len(S) == S.count("A"):
        return (len(S) * N) * (len(S) * N + 1) // 2
    else:
        tans = 0
        for c in S:
            k = 0 if c == "B" else k + 1
            tans += k
        return ans + (tans * (N - 1))


assert (solve(1, "AB") == 1)
assert (solve(1, "A") == 1)
assert (solve(1, "B") == 0)
assert (solve(100, "B") == 0)
assert (solve(100, "BBBBB") == 0)
assert (solve(100, "ABBBBB") == 100)
assert (solve(100, "BA") == 100)
assert (solve(2, "A") == 3)
assert (solve(2, "AA") == solve(1, "AAAA"))
assert (solve(4, "A") == solve(1, "AAAA"))
assert (solve(12, "A") == solve(1, "AAAAAAAAAAAA"))
assert (solve(4, "AAA") == solve(1, "AAAAAAAAAAAA"))
assert (solve(1, "AAB") == 3)
assert (solve(2, "AAB") == 6)
assert (solve(10, "AAB") == 30)
assert (solve(1, "ABA") == 2)
assert (solve(2, "ABA") == solve(1, "ABAABA"))
assert (solve(5, "ABA") == solve(1, "ABAABAABAABAABA"))

assert (solve(1, "AABA") == 4)
assert (solve(1, "AABAAABA") == 3 + 6 + 1)
assert (solve(2, "AABA") == 4 + 6)
assert (solve(3, "AABA") == 4 + 6 + 6)

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))
