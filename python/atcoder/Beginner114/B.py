def solve(S):
    return min([abs(753 - int(S[i:i + 3])) for i in range(0, len(S) - 2)])


if __name__ == "__main__":
    print(solve(input()))
