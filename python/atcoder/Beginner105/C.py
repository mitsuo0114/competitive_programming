def r(k):
    if k == -1:
        return 0, 0
    if k == 0:
        return 0, 1
    else:
        low, high = r(k - 1)
        d = pow(-2, k)
        if d < 0:
            return low + d, high
        else:
            return low, high + d


def solve(N):
    if N == 0:
        return "0"
    ar = []
    for k in range(50, -1, -1):
        low1, high1 = r(k - 1)
        low2, high2 = r(k)
        if not (low1 <= N <= high1) and low2 <= N <= high2:
            ar.append("1")
            N -= pow(-2, k)
        else:
            ar.append("0")
    ans = "".join(ar)
    ans = ans[ans.find("1"):]
    return ans


assert (solve(1) == "1")
assert (solve(-2) == "10")
assert (solve(-1) == "11")
assert (solve(4) == "100")
assert (solve(5) == "101")
assert (solve(16) == "10000")

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
