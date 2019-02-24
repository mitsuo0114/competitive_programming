import bisect

def solve(A, B, Q, Ss, Ts, Xs):
    ans = []
    Ss.append(10 ** 21)
    Ss.insert(0, -10 ** 21)
    Ts.append(10 ** 21)
    Ts.insert(0, -10 ** 21)
    for x in Xs:
        s_right = bisect.bisect_right(Ss, x)
        s_left = max(s_right - 1, 0)
        t_right = bisect.bisect_right(Ts, x)
        t_left = max(t_right - 1, 0)

        s_right = Ss[s_right]
        s_left = Ss[s_left]
        t_right = Ts[t_right]
        t_left = Ts[t_left]

        d_s_right = abs(s_right - x)
        d_s_left = abs(s_left - x)
        d_t_right = abs(t_right - x)
        d_t_left = abs(t_left - x)

        tans = 10 ** 35
        if x <= s_right and x <= t_right:
            tans = min(tans, max(d_t_right, d_s_right))
        if s_left <= x and t_left <= x:
            tans = min(tans, max(d_s_left, d_t_left))
        tans = min(tans, min(d_s_right, d_t_left) * 2 + max(d_s_right, d_t_left))
        tans = min(tans, min(d_t_right, d_s_left) * 2 + max(d_t_right, d_s_left))
        ans.append(str(tans))
    return "\n".join(ans)


assert (solve(1, 1, 1, [2], [0], [10]) == "10")
assert (solve(1, 1, 1, [200], [0], [10]) == "210")
assert (solve(1, 1, 1, [200], [0], [220]) == "220")
assert (solve(2, 2, 1, [2, 100], [0, 4], [3]) == "3")
assert (solve(2, 2, 1, [2, 100], [0, 4], [124]) == "120")
assert (solve(2, 2, 1, [2, 100], [0, 4], [0]) == "2")
assert (solve(2, 2, 1, [2, 100], [0, 4], [5]) == "3")

if __name__ == "__main__":
    A, B, Q = tuple(map(int, input().split(" ")))
    Ss = [int(input()) for _ in range(A)]
    Ts = [int(input()) for _ in range(B)]
    Xs = [int(input()) for _ in range(Q)]
    print(solve(A, B, Q, Ss, Ts, Xs))
