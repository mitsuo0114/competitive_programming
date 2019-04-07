def solve(N, Ts, Vs):
    print(N, ",", Ts, ",", Vs)
    startTs = [sum(Ts[:i]) for i in range(N)]
    endtime = startTs[-1] + Ts[-1]
    t = 0
    v = 0
    ans = 0
    while t <= endtime:
        t += 1
        ans += v

        maxes = [max(0, v + (start_t - t)) for start_t, v in zip(startTs, Vs) if start_t > t]
        maxes.extend([v for start_t, tt, v in zip(startTs, Ts, Vs) if start_t <= t <= start_t + tt])
        maxes.append(max(0, (endtime - t)))

        if v == min(maxes):
            pass
        elif v < min(maxes):
            v += 1
            ans += 0.5
        elif v > min(maxes):
            v -= 1
            ans -= 0.5
    return ans


assert (solve(2, [60, 50], [34, 38]) == 2632.0)
assert (solve(1, [100], [30]) == 2100.0)
assert (solve(3, [12, 14, 2], [6, 2, 7]) == 76.0)
assert (solve(10, [64, 55, 27, 35, 76, 119, 7, 18, 49, 100], [29, 19, 31, 39, 27, 48, 41, 87, 55, 70]) == 20291.0)

if __name__ == "__main__":
    N = int(input())
    Ts = list(map(int, input().split(" ")))
    Vs = list(map(int, input().split(" ")))
    print(solve(N, Ts, Vs))
