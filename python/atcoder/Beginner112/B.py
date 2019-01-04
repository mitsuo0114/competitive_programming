def solve(N):
    for i in range(N, 1000):
        if str(i)[2] == str(i)[1] == str(i)[0]:
            return i

if __name__ == "__main__":
    l = input()
    print(solve(int(l)))
