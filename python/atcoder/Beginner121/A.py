if __name__ == "__main__":
    H, W = tuple(map(int, input().split(" ")))
    h, w = tuple(map(int, input().split(" ")))
    print(H * W - h * W - w * H + w * h)
