def solve(n, As):
    odd = As[1::2]
    even = As[::2]
    if n % 2 == 0:
        return " ".join(map(str, odd[::-1] + even))
    else:
        return " ".join(map(str, even[::-1] + odd))


assert (solve(1, [1]) == "1")
assert (solve(2, [1, 2]) == "2 1")
assert (solve(3, [1, 2, 3]) == "3 1 2")
assert (solve(4, [1, 2, 3, 4]) == "4 2 1 3")
assert (solve(5, [1, 2, 3, 4, 5]) == "4 2 1 3 5"[::-1])

if __name__ == "__main__":
    n = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(n, As))
