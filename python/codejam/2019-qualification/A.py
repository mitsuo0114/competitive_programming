import math

t = int(input())
for i in range(1, t + 1):
  N = int(input())
  a = 0
  b = 0
  for d in str(N):
      a *= 10
      b *= 10
      d = int(d)
      if d >= 6:
          a += 6
          b += d - 6
      else:
          a += math.ceil(d / 2)
          b += math.floor(d / 2)
  print("Case #{}: {} {}".format(i, a, b))
