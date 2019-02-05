import math


def solve(N, CSFs):
    ans = []
    for k in range(0, len(CSFs)):
        t = 0
        for c, s, f in CSFs[k:]:
            if t < s:
                t = s
            else:
                t = f * math.ceil(t / f)
            t += c
        ans.append(t)
    ans.append(0)
    return "\n".join([str(t) for t in ans])


assert (solve(3, [(6, 5, 1), (1, 10, 1)]) == "12\n11\n0")
assert (solve(4, [(12, 24, 6), (52, 16, 4), (99, 2, 2)]) == "187\n167\n101\n0")
assert (solve(4, [(12, 13, 1), (44, 17, 17), (66, 4096, 64)]) == "4162\n4162\n4162\n0")

if __name__ == "__main__":
    N = int(input())
    CSFs = [tuple(map(int, input().split(" "))) for _ in range(N - 1)]
    print(solve(N, CSFs))
