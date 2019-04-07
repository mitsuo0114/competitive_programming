def solve(N, Q, S, LRs):
    Ts = [0 for _ in range(N)]
    tans = 0
    for i, (s1, s2) in enumerate(zip(S, S[1:])):
        if s1 == "A" and s2 == "C":
            tans += 1
        Ts[i + 1] = tans

    ans = []
    for l, r in LRs:
        ans.append(Ts[r - 1] - Ts[l - 1])
    return "\n".join(str(a) for a in ans)


assert (solve(8, 3, "ACACTACG", [(3, 7), (2, 3), (1, 8)]) == "2\n0\n3")
assert (solve(8, 3, "ACACTACG", [(1, 2)]) == "1")
assert (solve(8, 3, "ACACTACG", [(1, 3)]) == "1")
assert (solve(8, 3, "ACACTACG", [(1, 4)]) == "2")
assert (solve(8, 3, "ACACTACG", [(2, 3)]) == "0")
assert (solve(8, 3, "ACACTACG", [(2, 4)]) == "1")
assert (solve(6, 3, "ACACAC", [(5, 6)]) == "1")
assert (solve(6, 3, "ACACAC", [(1, 2)]) == "1")

if __name__ == "__main__":
    N, Q = tuple(map(int, input().split(" ")))
    S = input()
    LRs = [tuple(map(int, input().split(" "))) for __ in range(Q)]
    print(solve(N, Q, S, LRs))
