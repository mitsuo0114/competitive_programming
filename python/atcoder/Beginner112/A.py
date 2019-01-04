def solve(N):
    return l.replace("1", "8").replace("9", "1").replace("8", "9")

if __name__ == "__main__":
    l = input()
    print(solve(l))
