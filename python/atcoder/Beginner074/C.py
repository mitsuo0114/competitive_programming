def solve(A, B, C, D, E, F):
    sugers = set()
    for i in range(0, F // C + 1):
        for j in range(0, F // D + 1):
            s = (C * i + D * j)
            if s + 100 * s / E <= F:
                sugers.add(C * i + D * j)
            else:
                break
    sugers = sorted(list(sugers))

    waters = set()
    for i in range(0, F // A + 1):
        for j in range(0, F // B + 1):
            if (A * i + B * j) * 100 <= F:
                waters.add(A * i + B * j)
            else:
                break
    waters = sorted(list(waters))

    dense, w_all, w_suger = 0, A * 100, 0
    for s in sugers:
        for w in waters:
            if s + 100 * w <= F and s <= w * E and w + s > 0:
                densei = 100 * s / (100 * w + s)
                if dense < densei:
                    dense = densei
                    w_all = s + 100 * w
                    w_suger = s
                    break
    return " ".join([str(w_all), str(w_suger)])


assert (solve(1, 1, 1, 1, 1, 0) == "100 0")
assert (solve(1, 1, 1, 1, 1, 200) == "101 1")
assert (solve(1, 1, 1, 1, 1, 300) == "101 1")
assert (solve(1, 2, 10, 20, 15, 200) == "110 10")
assert (solve(1, 2, 1, 2, 100, 1000) == "200 100")
assert (solve(17, 19, 22, 26, 55, 2802) == "2634 934")

if __name__ == "__main__":
    A, B, C, D, E, F = map(int, input().split(" "))
    print(solve(A, B, C, D, E, F))
