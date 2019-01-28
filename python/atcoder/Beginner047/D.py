indexes = []


def dfs(Ds, s, e, v=None):
    if e - s == 1:
        if v == Ds[s]:
            indexes.append((s, e))
        return Ds[s]
    else:
        center = (s + e) // 2
        left = dfs(Ds, s, center, v=v)
        right = dfs(Ds, center, e, v=v)

        left_m = - (10 ** 9)
        li = -1
        su = 0
        for i in range(center-1, s-1, -1):
            su += Ds[i]
            if left_m != max(left_m, su):
                left_m = max(left_m, su)
                li = i

        right_m = -(10 ** 9)
        ri = -1
        su = 0
        for i in range(center, e):
            su += Ds[i]
            if right_m != max(right_m, su):
                right_m = max(right_m, su)
                ri = i

        if left_m + right_m == v:
            indexes.append((li, ri))

        m = max(left, right, left_m + right_m)
        return m


def solve(N, T, As):
    Ds = [As[i + 1] - As[i] for i in range(N - 1)]
    max_v = dfs(Ds, 0, N - 1)
    dfs(Ds, 0, N - 1, v=max_v)
    return len(indexes)


assert (dfs([-50, 150], 0, 2) == 150)
assert (dfs([-20, 10, -30, 10], 0, 4) == 10)
assert (dfs([3, -6, 1, 4, -6, 3, 2, -6, -1], 0, 9) == 5)
indexes = []
assert (solve(3, 2, [100, 50, 200]) == 1)
indexes = []
assert (solve(5, 8, [50, 30, 40, 10, 20]) == 2)
indexes = []
assert (solve(10, 100, [7, 10, 4, 5, 9, 3, 6, 8, 2, 1]) == 2)

indexes = []
if __name__ == "__main__":
    N, T = map(int, input().split(" "))
    As = list(map(int, input().split(" ")))
    print(solve(N, T, As))
