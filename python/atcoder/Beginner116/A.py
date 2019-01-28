if __name__ == "__main__":
    AB, BC, CA = tuple(map(int, input().split(" ")))
    if AB ** 2 + BC ** 2 == CA ** 2:
        print(AB * BC // 2)
    elif AB ** 2 + CA ** 2 == AB ** 2:
        print(AB * CA // 2)
    else:
        print(BC * CA // 2)
