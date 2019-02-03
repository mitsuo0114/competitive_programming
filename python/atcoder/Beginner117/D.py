def solve(N, K, As):
    Bs = ["{0:041b}".format(a) for a in As]
    ans = ""
    for i in range(0, 41):
        ck = sum([int(b[i]) for b in Bs])
        if ck > N - ck:
            ans += "0"
        else:
            ans += "1"

    Kstr = "{0:041b}".format(K)
    d = 0
    for k in range(1, 42):
        x = Kstr[:k-1] + "0" + ans[k:]
        X = int(x, 2)
        if X <= K:
            d = max(d, sum(X ^ a for a in As))
    return d


# assert ((solve(3, 0, [7, 7, 7])) == 21)
# assert ((solve(3, 8, [8, 8, 8])) == 45)
# assert ((solve(3, 7, [8, 8, 8])) == 45)
# assert ((solve(3, 0, [8, 8, 8])) == 24)
# assert ((solve(3, 8, [8, 6, 4])) == 16)
#assert ((solve(3, 21, [8, 6, 4])) == 16)
# assert ((solve(3, 7, [1, 6, 3])) == 14)
# assert ((solve(4, 9, [7, 4, 0, 3])) == 46)
# assert ((solve(1, 0, [1000000000000])) == 1000000000000)
# print("OK")
if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    As = list(map(int, input().split(" ")))
    print(solve(N, K, As))
