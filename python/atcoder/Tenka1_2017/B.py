def solve(N, AB):
    points = {}
    for ab in AB:
        a, b = ab[0], ab[1]
        points[a] = b
    c = 1
    As = sorted(points.keys())
    for i, a in enumerate(As):
        if i == 0:
            c += a
        elif i == len(As) - 1:
            c += points[a] + 1
        else:
            c += (As[i+1] - As[i])
    return c


if __name__ == "__main__":
    N= int(input())
    AB = [tuple(map(int, input().split(" "))) for i in range(N)]
    print(solve(N, AB))
