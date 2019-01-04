def solve(sx, sy, tx, ty):
    way1 = "R" * (tx - sx) + "U" * (ty - sy)
    way2 = "L" * (tx - sx) + "D" * (ty - sy)
    way3 = "D" + "R" * (tx - sx + 1) + "U" * (ty - sy+ 1) + "L"
    way4 = "U" + "L" * (tx - sx + 1) + "D" * (ty - sy+ 1) + "R"
    return way1 + way2 + way3 + way4

if __name__ == "__main__":
    sx, sy, tx, ty = map(int, input().split(" "))
    print(solve(sx, sy, tx, ty))
