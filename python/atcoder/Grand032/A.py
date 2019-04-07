def solve(N, Bs):
    ans = []
    while len(Bs):
        failed = True
        for i, b in enumerate(Bs[::-1]):
            i = len(Bs) - i
            if i == b:
                ans.append(Bs.pop(i - 1))
                failed = False
                break
        if failed:
            return "-1"
    return "\n".join(str(a) for a in ans[::-1])


assert (solve(1, [1]) == "1")
assert (solve(3, [1, 2, 1]) == "1\n1\n2")
assert (solve(3, [1, 1, 1]) == "1\n1\n1")
assert (solve(9, [1, 1, 1, 2, 2, 1, 2, 3, 2]) == "1\n2\n2\n3\n1\n2\n2\n1\n1")
assert (solve(3, [1, 2, 3]) == "1\n2\n3")
assert (solve(2, [1, 1]) == "1\n1")
assert (solve(2, [1, 1, 3]) == "1\n1\n3")
assert (solve(2, [1, 2, 2]) == "1\n2\n2")
assert (solve(1, [2]) == "-1")
assert (solve(3, [2, 2, 2]) == "-1")

if __name__ == "__main__":
    N = int(input())
    bs = list(map(int, input().split(" ")))
    print(solve(N, bs))
