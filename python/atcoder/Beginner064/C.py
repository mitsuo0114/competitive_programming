def solve(N, As):
    colors = set()
    allcount = 0
    for a in As:
        n = a // 400
        if n < 8:
            colors.add(n)
        else:
            allcount += 1
    return max(len(colors), 1), len(colors) + allcount


if __name__ == "__main__":
    N = int(input())
    As = map(int, input().split(" "))
    m1, m2 = solve(N, As)
    print(m1, m2)
