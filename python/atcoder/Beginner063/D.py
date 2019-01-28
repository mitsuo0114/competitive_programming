import math


def solve(N, A, B, Hs):
    k_min = 1
    k_max = 10 ** 9
    d = A - B
    # print(N, ",", A, ",", B, ",", Hs)

    def find(k):
        # print("find %d" % k)
        kc = sum([max(math.ceil((h - B * k) / d), 0) for h in Hs])
        return kc <= k

    def bin_search(k_min, k_max):
        if k_max - k_min <= 1:
            if find(k_min):
                return k_min
            return k_max
        # print("find %d, %d" % (k_min, k_max))
        k_mid = (k_max + k_min) // 2
        m = find(k_mid)
        if m:
            return bin_search(k_min, k_mid)
        else:
            return bin_search(k_mid, k_max)

    return bin_search(k_min, k_max)

assert (solve(4, 7, 6, [1, 1, 1, 1]) == 1)
assert (solve(4, 5, 3, [8, 7, 4, 2]) == 2)
assert (solve(2, 10, 4, [20, 20]) == 4)
assert (solve(5, 2, 1, [900000000, 900000000, 1000000000, 1000000000, 1000000000]) == 800000000)

if __name__ == "__main__":
    N, A, B = tuple(map(int, input().split(" ")))
    Hs = []
    for _ in range(N):
        Hs.append(int(input()))
    print(solve(N, A, B, Hs))
