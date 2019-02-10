def solve(K, A, B):
    if B - A <= 2:
        return K + 1
    elif K <= A:
        return K + 1
    else:
        K -= (A - 1)
        if K <= 2:
            return (K // 2) * B
        else:
            if K % 2 == 0:
                return B + (K // 2 - 1) * (B - A)
            else:
                return B + (K // 2 - 1) * (B - A) + 1


assert (solve(3, 2, 6) == 6)
assert (solve(4, 2, 6) == 7)
assert (solve(5, 2, 6) == 6 - 2 + 6)
assert (solve(6, 2, 6) == 6 - 2 + 6 + 1)
assert (solve(7, 2, 6) == 6 - 2 + 6 - 2 + 6)
assert (solve(3, 2, 100) == 100)
assert (solve(7, 3, 4) == 8)
assert (solve(314159265, 35897932, 384626433) == 48518828981938099)
assert (solve(10, 100, 1) == 11)
assert (solve(10, 100, 200) == 11)

if __name__ == "__main__":
    K, A, B = tuple(map(int, input().split(" ")))
    print(solve(K, A, B))
