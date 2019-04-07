
def solve(N, Ps):
    ans = 0
    for i in range(1, N):
        if Ps[i - 1] == i and Ps[i] == i + 1:
            Ps[i - 1] = i + 1
            Ps[i] = i
            ans += 1
    ans += sum(1 for i in range(N) if Ps[i] == i + 1)
    return ans


assert (solve(5, [1, 4, 3, 5, 2]) == 2)

if __name__ == "__main__":
    N = int(input())
    Ps = list(map(int, input().split(" ")))
    print(solve(N, Ps))
