if __name__ == "__main__":
    A, B, C = tuple(map(int, input().split(" ")))
    print(min(C, B // A))
