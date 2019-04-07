def solve(N, Q, S, TDs):
    f_index = -1
    l_index = N
    ans = N
    for q in TDs[::-1]:
        t, d = q
        if d == "L" and 0 <= f_index + 1 < N and S[f_index + 1] == t:
            f_index += 1
            ans -= 1
        elif d == "R" and 0 <= l_index - 1 < N and S[l_index - 1] == t:
            l_index -= 1
            ans -= 1

        elif d == "R" and 0 <= f_index + 1 < N and S[f_index + 1] == t:
            f_index = -10
        elif d == "L" and 0 <= l_index - 1 < N and S[l_index - 1] == t:
            l_index = -10

    return max(0, ans)


#
#
assert (solve(3, 1, "ABC", [("A", "L")]) == 2)
assert (solve(3, 2, "ABC", [("B", "R"), ("C", "R")]) == 1)

assert (solve(3, 3, "ABC", [("B", "R"), ("C", "R"), ("B", "L"), ("A", "L")]) == 0)
assert (solve(3, 3, "ABC", [("B", "R"), ("C", "L"), ("B", "L"), ("A", "L")]) == 0)
assert (solve(3, 3, "ABC", [("B", "R"), ("B", "L"), ("A", "L")]) == 2)
assert (solve(3, 3, "ABC", [("A", "R"), ("B", "R"), ("C", "L"), ("B", "L")]) == 3)
assert (solve(3, 3, "ABC", [("A", "R"), ("B", "R"), ("C", "L"), ("B", "L"), ("A", "L")]) == 0)
assert (solve(3, 3, "ABC", [("C", "L"), ("B", "L"), ("A", "R"), ("B", "R")]) == 3)
assert (solve(3, 3, "ABC", [("C", "L"), ("B", "L"), ("A", "R"), ("B", "R"), ("C", "R")]) == 0)

assert (solve(3, 3, "ABC", [("A", "R"), ("B", "R"), ("C", "R")]) == 0)
assert (solve(3, 3, "ABC", [("A", "L"), ("B", "L"), ("C", "L")]) == 2)
assert (solve(3, 3, "ABC", [("C", "L"), ("B", "L"), ("A", "L")]) == 0)
assert (solve(3, 3, "ABC", [("B", "L"), ("B", "L"), ("B", "L")]) == 3)
assert (solve(3, 3, "ABC", [("C", "L"), ("C", "L"), ("C", "L")]) == 3)
assert (solve(3, 3, "ABC", [("A", "L"), ("A", "L"), ("A", "L")]) == 2)
assert (solve(3, 1, "ABC", [("C", "R")]) == 2)
assert (solve(3, 2, "ABC", [("A", "L"), ("A", "L")]) == 2)

assert (solve(3, 3, "AAA", [("A", "L"), ("A", "L"), ("A", "L"), ("A", "L")]) == 0)
assert (solve(3, 3, "AAA", [("A", "L"), ("A", "L"), ("A", "L")]) == 0)
assert (solve(3, 3, "AAA", [("A", "L"), ("A", "L")]) == 1)
assert (solve(3, 3, "AAA", [("A", "L")]) == 2)

assert (solve(3, 3, "AAA", [("A", "R"), ("A", "R"), ("A", "R"), ("A", "R"), ("A", "R")]) == 0)
assert (solve(3, 3, "AAA", [("A", "R"), ("A", "R"), ("A", "R")]) == 0)
assert (solve(3, 3, "AAA", [("A", "R"), ("A", "R")]) == 1)
assert (solve(3, 3, "AAA", [("A", "R")]) == 2)

if __name__ == "__main__":
    N, Q = tuple(map(int, input().split(" ")))
    S = input()
    TDs = [tuple(input().split(" ")) for __ in range(Q)]
    print(solve(N, Q, S, TDs))
