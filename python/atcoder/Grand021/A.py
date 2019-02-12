def solve(N):
    if N < 10:
        return N
    num = int("9" * (len(str(N)) - 1))
    k = int(str(N)[0] + str(num))
    if k <= N:
        return sum(int(c) for c in str(k))
    else:
        k = k - num - 1
        return sum(int(c) for c in str(k))


assert (solve(799) == 25)
assert (solve(999) == 27)
assert (solve(200) == 19)
assert (solve(100) == 18)
assert (solve(99) == 18)
assert (solve(89) == 17)
assert (solve(5) == 5)

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
