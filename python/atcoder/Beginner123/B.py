from itertools import permutations


def solve(a, b, c, d, e):
    m = 10000
    for p in permutations([a, b, c, d, e]):
        t = 0
        for i, o in enumerate(p):
            t += o
            if i == len(p) - 1:
                break
            while t % 10 != 0:
                t += 1
        m = min(t, m)
    return m


# solve(1, 2, 3, 4, 5)
# print(solve(29,20,7,35,120))
print(solve(123, 123, 123, 123, 123))

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(solve(a, b, c, d, e))
