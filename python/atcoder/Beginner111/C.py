def solve(C):
    C.sort(key=lambda x: x[2], reverse=True)
    for xi in range(0, 101):
        for yi in range(0, 101):
            h = C[0][2] + abs(xi - C[0][0]) + abs(yi - C[0][1])
            if all(max(h - abs(xi - c[0]) - abs(yi - c[1]), 0) == c[2] for c in C):
                return [str(xi), str(yi), str(h)]


if __name__ == "__main__":
    N = int(input())
    C = []
    for n in range(N):
        d = input().split(" ")
        C.append((int(d[0]), int(d[1]), int(d[2])))
    print(" ".join(solve(C)))
