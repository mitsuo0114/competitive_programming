def solve(N):
    ret = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ret.append(max(len(str(i)),
                           len(str(N // i))))
    return min(ret)


if __name__ == "__main__":
    N = int(input())
    print(solve(N))
