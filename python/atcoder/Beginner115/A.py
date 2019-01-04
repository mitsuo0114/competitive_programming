def solve(X):
    return ("Christmas " + " ".join(["Eve"] * (25 - X))).strip()

if __name__ == "__main__":
    print(solve(int(input())))
