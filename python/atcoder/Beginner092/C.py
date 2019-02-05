def solve(N, As):
    costs = [abs(As[0])]
    costs.extend([abs(s - d) for s, d in zip(As, As[1:])])
    s = sum(costs) + abs(As[-1])

    skipcosts = [abs(As[1])]
    skipcosts.extend([abs(s - d) for s, d in zip(As, As[2:])])
    skipcosts.append(0)
    ans = []
    for i, c in enumerate(skipcosts):
        if i < N - 1:
            ans.append(str(s - costs[i] - costs[i + 1] + c))
        else:
            ans.append(str(s - costs[i] - abs(As[-1]) + abs(As[-2])))
    return "\n".join(ans)


assert (solve(3, [5, -5, 5]) == "20\n10\n20")
assert (solve(3, [1, 2, 3]) == "6\n6\n4")
assert (solve(3, [-1, 2, 3]) == "6\n8\n6")
assert (solve(3, [3, 5, -1]) == "12\n8\n10")

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
