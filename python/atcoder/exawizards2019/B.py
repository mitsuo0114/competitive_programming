def solve(N, s):
    return "Yes" if s.count("R") - s.count("B") > 0 else "No"

if __name__ == "__main__":
    N = int(input())
    s = input()
    print(solve(N, s))
