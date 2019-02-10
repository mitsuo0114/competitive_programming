def solve(S, K):
    for s in S[:K]:
        if s != "1":
            return s
    return "1"


assert (solve("1", 1) == "1")
assert (solve("12", 2) == "2")
assert (solve("112", 2) == "1")
assert (solve("112", 3) == "2")

if __name__ == "__main__":
    S = input()
    K = int(input())
    print(solve(S, K))
