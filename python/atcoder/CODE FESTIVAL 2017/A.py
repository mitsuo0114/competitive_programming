import re


def solve(S):
    return "YES" if re.findall("^A?KIHA?BA?RA?$", S) else "NO"


assert (solve("AKIHABARA") == "YES")
assert (solve("AKIHABARAA") == "NO")
assert (solve("KIHBR") == "YES")
assert (solve("AKIBAHARA") == "NO")
assert (solve("AAKIAHBAARA") == "NO")

if __name__ == "__main__":
    print(solve(input()))
