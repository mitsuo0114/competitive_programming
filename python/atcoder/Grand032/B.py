from itertools import combinations
def p(mat):
    [print(l) for l in mat]
    print()

def solve(N):
    mat = [ [ 0 if i + 1 == j + 1 else i + 1 for i in range(N)  ] for j in range(N) ]
    p(mat)
    mat2 = [ [ -1 if i + 1 == j + 1 else 0 for i in range(N)  ] for j in range(N) ]


    all_candidate = set()
    for m in mat:
        candidate1 = set()
        for i in range(1, N):
            for k in combinations(m, i):
                candidate1.add(sum(k))
        if not len(all_candidate):
            all_candidate = candidate1
        else:
            all_candidate = set(all_candidate).intersection(candidate1)
    all_candidate.remove(0)
    # print(list(all_candidate))

    target = max(list(all_candidate)) - 6
    candidates = [[] for n in range(N)]
    for n, m in enumerate(mat):
        candidate = []
        for i in range(1, N):
            for k in combinations([d for d in m if d != 0], i):
                if sum(k) == target:
                    candidates[n].append(k)
    p(candidates)



#solve(3)
#solve(4)
# solve(5)
solve(6)
# solve(100)
# assert (solve(3) == "1")

if __name__ == "__main__":
    N = int(input())
    print(solve(N))
