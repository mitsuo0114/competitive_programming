def solve(N, A, B):
    f = "{:0%db}" % N
    AStr = f.format(A)
    BStr = f.format(B)
    rAStr = "".join(["1" if c == "0" else "0" for c in f.format(A)])
    rBStr = "".join(["1" if c == "0" else "0" for c in f.format(B)])
    d2 = sum(abs(int(a) - int(b)) for a, b in zip(rAStr, rBStr))

    dr1 = sum(abs(int(a) - int(b)) for a, b in zip(rAStr, BStr))
    dr2 = sum(abs(int(a) - int(b)) for a, b in zip(AStr, rBStr))

    if N == 1:
        ans = [A, B]
        return "\n".join(["YES", " ".join([str(a) for a in ans])])

    if dr1 + dr2 + d2 == 2**N - 1:
        same_i = -1
        for i, (ra, b) in enumerate(zip(rAStr, rBStr)):
            if ra != b:
                same_i = i


        AStr = list(AStr)
        ans = [int("".join(AStr), 2)]


        for _ in range(2 ** N // 2):
            for i, (a, b) in enumerate(zip(AStr, rBStr)):
                if a != b and i != same_i:
                    AStr[i] = b
                    ans.append(int("".join(AStr), 2))

        AStr[same_i] = rAStr[same_i]
        ans.append(int("".join(AStr), 2))

        for _ in range(2 ** N // 2):
            for i, (a, b) in enumerate(zip(AStr, BStr)):
                if a != b:
                    AStr[i] = b
                    ans.append(int("".join(AStr), 2))
        return "\n".join(["YES", " ".join([str(a) for a in ans])])
    else:
        return "NO"


assert (solve(1, 1, 0) == "YES\n1 0")
assert (solve(1, 0, 1) == "YES\n0 1")
assert (solve(2, 1, 2) == "NO")
# assert (solve(2, 1, 3) == "YES\n1 0 2 3")
#assert (solve(3, 5, 7) == "YES\n5 0 2 6 7")
assert (solve(3, 6, 7) == "YES\n5 4 0 1 3 6 7")

if __name__ == "__main__":
    N, A, B = tuple(map(int, input().split(" ")))
    print(solve(N, A, B))
