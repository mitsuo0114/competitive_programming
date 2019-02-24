def tsolve(N, S, i=-1):
    ans = 0
    k = 2
    for si, c in enumerate(S):
        if c == ">" or si == i:
            ans += 1 / k
            k += 1
        else:
            ans += 1
            k = 2
    if i == -1:
        return "{:.14f}".format(ans)
    else:
        return ans


assert (tsolve(3, "---") == "3.00000000000000")
assert (tsolve(4, "----") == "4.00000000000000")
assert (tsolve(5, "-->--") == "4.50000000000000")
assert (tsolve(6, "-->>--") == "4.83333333333333")


def solve(N, S):
    m = tsolve(N, S, 0)
    k = 0
    km = 0
    for i in range(N - 1):
        if S[i] == "-" and S[i - 1] == ">":
            if k > km:
                m = min(m, tsolve(N, S, i))
            km = max(k, km)
            k = 0
        else:
            k += 1
    return "{:.14f}".format(m)


assert (solve(5, "-->--") == "3.83333333333333")
assert (solve(7, "-------") == "6.50000000000000")
assert (solve(10, "-->>>-->--") == "6.78333333333333")

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))
