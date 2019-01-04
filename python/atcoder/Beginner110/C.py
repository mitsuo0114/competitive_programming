def solve(S, T):
    sm = {}
    tm = {}
    for s, t in zip(S, T):
        if s in sm and sm[s] != t:
            return "No"
        sm[s] = t

        if t in tm and tm[t] != s:
            return "No"
        tm[t] = s

    return "Yes"


if __name__ == "__main__":
    S = input()
    T = input()
    print(solve(S, T))
