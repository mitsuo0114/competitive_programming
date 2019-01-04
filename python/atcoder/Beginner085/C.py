def solve(N, Y):
    r = [5000 for _ in range(N)]
    for i in range(N + 1):
        s = sum(r)
        if s == Y:
            return (
            len([d for d in r if d == 10000]), len([d for d in r if d == 5000]), len([d for d in r if d == 1000]))
        elif s < Y and i < N:
            r[i] = 10000
        elif s > Y and i < N:
            r[i] = 1000
    return (-1, -1, -1)


if __name__ == "__main__":
    N, Y = tuple(map(int, input().split(" ")))
    print(" ".join(map(str, list(solve(N, Y)))))
