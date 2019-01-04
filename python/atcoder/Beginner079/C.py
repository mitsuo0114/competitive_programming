def solve(ABCD):
    for i in range(0, 8):
        ops = "{:03b}".format(i)
        op1 = "+" if ops[0] == "0" else "-"
        op2 = "+" if ops[1] == "0" else "-"
        op3 = "+" if ops[2] == "0" else "-"
        s = ABCD[0] + op1 + ABCD[1] + op2 + ABCD[2] + op3 + ABCD[3]
        if eval(s) == 7:
            return s + "=7"
    return "error"


if __name__ == "__main__":
    ABCD = input()
    print(solve(ABCD))
