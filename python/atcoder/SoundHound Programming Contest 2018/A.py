def solve(C, D):
    ans = 0
    while D >= 140:
        print(C, D)
        si, ei = 140, 170
        while ei < 10 ** 15 + 1:
            if D < si:
                pass
            elif si <= C < ei and si <= D < ei:
                ans += D - C
            elif C <= si and si <= D < ei:
                ans += D - si
            elif si <= C < ei and D < ei:
                ans += ei - C
            elif C <= si and ei < D:
                ans += ei - si - 1
            si *= 2
            ei *= 2
        C //= 2
        D //= 2
    return ans


# assert (solve(139, 141) == 1)
assert (solve(140, 142) == 2)
assert (solve(141, 143) == 2)
assert (solve(140, 180) == 29)
assert (solve(160, 300) == 30)

if __name__ == "__main__":
    C, D = tuple(map(int, input().split(" ")))
    print(solve(C, D))
