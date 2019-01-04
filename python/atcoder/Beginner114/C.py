from itertools import product

def solve(N):
    sum = 0
    for k in range(1, 10):
        for i in product('357', repeat=k):
            if '3' in i and '5' in i and '7' in i:
                d = int("".join(list(i)))
                if d <= N:
                    sum += 1
    return sum


if __name__ == "__main__":
    print(solve(int(input())))
