from collections import Counter
from math import factorial


def solve(N, A, B, Vs):
    Vs.sort(reverse=True)

    all_counter = Counter(Vs)
    first = Vs[:A]
    first_c = Counter(Vs[:A])

    second_c = Counter(Vs[A:])
    avg = sum(first) / A

    ans = 1
    for fv, fc in first_c.items():
        if fv == avg:
            ts = 0
            for c in range(A, min(all_counter[fv], B) + 1):
                ts += factorial(all_counter[fv]) // factorial(c) // factorial(all_counter[fv] - c)
            ans *= ts
        else:
            ans *= factorial(all_counter[fv]) // factorial(second_c[fv]) // factorial(fc)
    return "\n".join(["{:0.6f}".format(avg), str(ans)])

assert(solve(5, 1, 1, [5, 5, 5, 5]) == "5.000000\n4")
assert(solve(5, 1, 2, [5, 5, 5, 5]) == "5.000000\n10")
assert(solve(5, 2, 2, [5, 5, 5, 5]) == "5.000000\n6")

assert(solve(5, 1, 2, [1, 2, 3, 4, 5]) == "5.000000\n1")
assert(solve(5, 3, 2, [4, 4, 3, 4, 5]) == "4.333333\n3")
assert(solve(5, 4, 2, [4, 4, 3, 4, 5]) == "4.250000\n1")

assert(solve(5, 2, 2, [1, 2, 3, 4, 5]) == "4.500000\n1")
assert(solve(4, 2, 3, [10, 20, 10, 10]) == "15.000000\n3")
assert(solve(5, 1, 5, [1000000000000000, 999999999999999, 999999999999998, 999999999999997, 999999999999996]) ==
       "1000000000000000.000000\n1")
assert(solve(50, 1, 50, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) ==
       "1.000000\n1125899906842623")

if __name__ == "__main__":
    N, A, B = map(int, input().split(" "))
    Vs = list(map(int, input().split(" ")))
    print(solve(N, A, B, Vs))
