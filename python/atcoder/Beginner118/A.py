if __name__ == "__main__":
    A, B = tuple(map(int, input().split(" ")))
    print (A + B if B % A == 0 else  B- A)