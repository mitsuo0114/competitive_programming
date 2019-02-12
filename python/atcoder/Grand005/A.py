def solve(X):
    ans = 0
    count = 0
    for c in X:
        if c == "S":
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                ans += 1
    ans += count
    return ans

assert(solve("TS") == 2)
assert(solve("ST") == 0)
assert(solve("STST") == 0)
assert(solve("SSTT") == 0)
assert(solve("SSTTT") == 1)
assert(solve("SSSTT") == 1)

if __name__ == "__main__":
    X = input()
    print(solve(X))
