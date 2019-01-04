def solve(X, Y):
    X, Y = max(X, Y), min(X, Y)
    X3, X1 = X // 3, X % 3
    Y3, Y1 = Y // 3, Y % 3
    if X == Y * 3 or (X3 == Y1 and Y3 == X1):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    X, Y = tuple([int(c) for c in input().split(" ")])
    print(solve(X, Y))
