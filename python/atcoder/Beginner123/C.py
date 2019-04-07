import math
def solve(n, a, b, c, d, e):
    return math.ceil(n / min(a, b, c, d, e)) + 4



if __name__ == "__main__":
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(solve(n, a, b, c, d, e))
