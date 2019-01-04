from itertools import combinations


def solve(N, Ss):
    caps = {c: set() for c in 'MARCH'}
    for s in Ss:
        caps.setdefault(s[0], set()).add(s)
    sum = 0
    for d in combinations('MARCH', 3):
        sum += len(caps[d[0]]) * len(caps[d[1]]) * len(caps[d[2]])
    return sum


if __name__ == "__main__":
    N = int(input())
    Ss = [input() for _ in range(N)]
    print(solve(N, Ss))
