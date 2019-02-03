def solve(N, Ls):
    if max(Ls) < sum(Ls) - max(Ls):
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    N = int(input())
    Ls = list(map(int, input().split(" ")))
    print(solve(N, Ls))
