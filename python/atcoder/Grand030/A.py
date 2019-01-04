def solve(A, B, C):
    return B + min(C, B) + min(A+1, C - min(C, B))

# assert(solve(3, 1, 4) == 5)
# assert(solve(5, 2, 9) == 10)
# assert(solve(8, 8, 1) == 9)
# assert(solve(0, 100, 0) == 100)

if __name__ == "__main__":
    l = input().split()
    A, B, C = int(l[0]), int(l[1]), int(l[2])
    print(solve(A, B, C))
