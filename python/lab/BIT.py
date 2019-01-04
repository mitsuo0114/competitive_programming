
A = [2, 3, 4, 1] # => 3

count = 0
swapset = []
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        if A[j] < A[i]:
            swapset.append( (i, j) )

# print(count)
print(swapset)
n = len(A)
BIT = [0 for _ in range(0, n + 1)]

def add(i, x):
    while i <= n:
        BIT[i] += x
        i += i & (-i)

for i in range(0, n):
    add(i + 1, A[i])

def mysum(i):
    s = 0
    while(i > 0):
        s += BIT[i]
        i = i & (i-1)
    return s
#
# A = [2, 3, 4, 1] # => 3

# D = [sum(S[0:j+1]) for j in range(0, len(A))]
print(A)
print(BIT[1:])
S = [mysum(j) for j in range(1, len(A) + 1)]
print(S)

Sj = []
for j in range(0, len(A)):
    Sj.append(j - mysum(A[j]))
    add(A[j], 1)

print(sum(Sj))
# print(S)
# print(D)
# print(sum(D))