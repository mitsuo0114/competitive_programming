if __name__ == "__main__":
    Y, M, D = tuple(map(int, input().split("/")))
    if Y <= 2018:
        print("Heisei")
    if Y == 2019 and M < 5:
        print("Heisei")
    else:
        print("TBD")
