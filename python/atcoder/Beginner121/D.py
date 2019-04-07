def slow_solve(A, B):
    ans = A
    for i in range(A + 1, B + 1):
        ans = ans ^ i
    return ans


def count(k, cycle):
    k += 1
    tans = (k // cycle) * (cycle // 2)
    res = k % cycle
    if res >= cycle // 2:
        tans += res % (cycle // 2)
    return tans


assert (count(8, 8) == 4)
assert (count(7, 8) == 4)
assert (count(6, 8) == 3)
assert (count(5, 8) == 2)
assert (count(4, 8) == 1)
assert (count(3, 8) == 0)
assert (count(2, 8) == 0)
assert (count(1, 8) == 0)
assert (count(0, 8) == 0)

assert (count(8, 4) == 4)
assert (count(7, 4) == 4)
assert (count(6, 4) == 3)
assert (count(5, 4) == 2)
assert (count(4, 4) == 2)
assert (count(3, 4) == 2)
assert (count(2, 4) == 1)
assert (count(1, 4) == 0)
assert (count(0, 4) == 0)

assert (count(8, 2) == 4)
assert (count(4, 2) == 2)
assert (count(3, 2) == 2)
assert (count(2, 2) == 1)
assert (count(1, 2) == 1)
assert (count(0, 2) == 0)


def solve(A, B):
    cycle = 2
    ans = ""
    for _ in range(40):
        acount = count(A - 1, cycle)
        bcount = count(B, cycle)
        ans = str((bcount - acount) % 2) + ans
        cycle *= 2
    return int(ans, base=2)


assert (slow_solve(2, 4) == solve(2, 4))
assert (slow_solve(2, 5) == solve(2, 5))
assert (slow_solve(2, 6) == solve(2, 6))
assert (slow_solve(2, 7) == solve(2, 7))

assert (solve(1, 1) == 1)
assert (solve(2, 4) == 5)
assert (solve(123, 456) == 435)

if __name__ == "__main__":
    A, B = tuple(map(int, input().split(" ")))
    print(solve(A, B))
