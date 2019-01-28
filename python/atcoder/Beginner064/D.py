def solve(N, S):
    # print(N, ",", S)
    balance = 0
    start = 0
    for i in range(N):
        if S[i] == ")":
            if balance == 0:
                start += 1
            else:
                balance -= 1
        else:
            balance += 1
    return "(" * start + S + ")" * balance

assert (solve(2, "()") == "()")
assert (solve(4, "()()") == "()()")
assert (solve(4, "(())") == "(())")
assert (solve(1, ")") == "()")
assert (solve(1, "(") == "()")
assert (solve(2, "))") == "(())")
assert (solve(2, "((") == "(())")
assert (solve(2, ")(") == "()()")
assert (solve(3, "())") == "(())")
assert (solve(6, ")))())") == "(((()))())")
assert (solve(8, "))))((((") == "(((())))(((())))")

if __name__ == "__main__":
    N = int(input())
    S = input()
    print(solve(N, S))
