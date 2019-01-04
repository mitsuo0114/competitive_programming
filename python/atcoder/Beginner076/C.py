def solve(S, T):
    for i in reversed(range(0, len(S) - len(T) + 1)):
        if all(S[j] == "?" or S[j] == T[j - i] for j in range(i, i + len(T))):
            return (S[0:i] + T + S[i + len(T):]).replace("?", "a")
    return "UNRESTORABLE"


if __name__ == "__main__":
    S = input()
    T = input()
    print(solve(S, T))
