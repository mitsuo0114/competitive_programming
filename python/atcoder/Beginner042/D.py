import math

def solve(H, W, A, B):
    K = math.factorial(H - A + B) * math.factorial(W - B + A)

    D = math.factorial(H - A) * math.factorial(B) * math.factorial(W - B) * math.factorial(A)
    print(K, D)
    i = 1
    sum = 0
    while A + i <= H and B + i <= W:
        sum += K // D
        D *= A + i
        D *= B + i
        D //= (H-A)
        D //= (W-B)
        i += 1

    print(sum)

assert(solve(2,2,0,0) == 2)
assert(solve(2,3,1,1) == 2)

if __name__ == "__main__":
    H, W, A, B = map(int, input().split(" "))
    print(solve(H, W, A, B))
