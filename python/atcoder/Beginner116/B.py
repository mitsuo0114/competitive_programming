def solve(s):
    d = set()

    def f(i):
        if i % 2 == 0:
            return i // 2
        else:
            return 3 * i + 1

    while True:
        d.add(s)
        s = f(s)
        if s in d:
            return len(d) + 1


if __name__ == "__main__":
    s = int(input())
    print(solve(s))
