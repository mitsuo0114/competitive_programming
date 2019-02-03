def solve(H, W, N, As):
    # print(H, ",", W, ",", N, ",", As)
    field = [[0] * W for _ in range(H)]
    index = 0
    for color, a in enumerate(As):
        color += 1
        for _ in range(a):
            row = index // W
            if row % 2 == 0:
                field[row][index - row * W] = str(color)
            else:
                field[row][W - (index - row * W) - 1] = str(color)
            index += 1
    ans = "\n".join([" ".join(row) for row in field])
    return ans


# print(solve(2, 2, 3, [2, 1, 1]))

if __name__ == "__main__":
    H, W = tuple(map(int, input().split(" ")))
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(H, W, N, As))
