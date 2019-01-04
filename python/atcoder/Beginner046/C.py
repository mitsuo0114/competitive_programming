import math
from itertools import combinations

def solve(S):
    l = 2 ** (len(S) - 1)
    sum = 0
    for i in range(l):
        bi = ("{:0%db}" % (len(S) - 1)).format(i)
        ope = []
        for b in bi:
            if b == "0":
                ope.append("")
            else:
                ope.append("+")
        ope.append("")
        p = ""
        for s, o in zip(S, ope):
            p += s
            p += o
        sum += eval(p)
    return sum


if __name__ == "__main__":
    print(solve(input()))

# print(solve(4, 8, [7, 9, 8, 9]))
# print(solve(8, 5, [3, 6, 2, 8, 7, 6, 5, 9]))
# print(solve(33, 3, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
