def solve(T, A, B, C, D):
    if A + C <= T:
        return B + D
    elif C <= T:
        return D
    elif A <= T:
        return B
    else:
        return 0


if __name__ == "__main__":
    T, A, B, C, D = tuple([int(c) for c in input().split(" ")])
    print(solve(T, A, B, C, D))
