def solve(c1, c2, c3):
    if (c1[0] + c2[1] + c3[2]) * 3 == sum(c1) + sum(c2) + sum(c3):
        return "Yes"
    return "No"


if __name__ == "__main__":
    c1 = list(map(int, input().split(" ")))
    c2 = list(map(int, input().split(" ")))
    c3 = list(map(int, input().split(" ")))
    print(solve(c1, c2, c3))
