A, B, C = tuple(map(int, input().split(" ")))
print("Yes" if A==B and B==C and A==C else "No")