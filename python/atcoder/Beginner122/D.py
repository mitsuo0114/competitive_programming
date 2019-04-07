from itertools import product

def slow_solve(N):
    for k in product("ACGT", repeat=N):
        str = "".join(list(k))
        if any(bad in str for bad in ["AGC", "GAC", "ACG",
                                      "AAGC","ACGC","AGGC","ATGC",
                                      "AGAC","AGCC","AGGC","AGTC"] ):
                print(str)

slow_solve(3)
print("----")
slow_solve(4)


def solve(N):
    Ts = [0 for i in range(N+1)]
    Ts[0] = 1
    Ts[1] = 4
    Ts[2] = 16
    Ts[3] = 61
    d = 10 ** 9 + 7
    for i in range(3, N):
        Ts[i + 1] = (Ts[i] * 4 - Ts[i-2] * 2 - Ts[i-3]*6)
        print(f"{Ts[i + 1]} = {Ts[i] * 2} - {Ts[i-3]*6}")
        print(Ts)

    return Ts[N] % d

solve(4)
solve(5)
#
# assert (slow_solve(2, 4) == solve(2, 4))
# assert (slow_solve(2, 5) == solve(2, 5))
# assert (slow_solve(2, 6) == solve(2, 6))
# assert (slow_solve(2, 7) == solve(2, 7))
#
# assert (solve(1, 1) == 1)
# assert (solve(2, 4) == 5)
# assert (solve(123, 456) == 435)

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
