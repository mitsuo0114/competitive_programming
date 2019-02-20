def solve(N):
    d = 10 ** 7
    index = d // 2
    while True:
        k1 = index * (index - 1) // 2
        k2 = index * (index + 1) // 2
        if k1 < N <= k2:
            break
        elif k1 <= N:
            index = (index + d) // 2
        else:
            d = index
            index = index // 2

    d = k2 - N
    return "\n".join([str(i) for i in range(1, index + 1) if i != d])


assert (solve(1) == "1")
assert (solve(2) == "2")
assert (solve(4) == "1\n3")
assert (solve(10) == "1\n2\n3\n4")

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
