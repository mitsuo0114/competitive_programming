from sys import stderr, stdout

def solve(N, B, F):
    outputs = ["" for _ in range(F)]
    for i in range(N):
        b = "{:010b}".format(i)
        for d in range(F):
            outputs[d] += b[d]

    response = []
    for out in outputs:
        print(out, flush=True)
        stdout.flush()
        response.append(input())

    resdata = ["" for _ in range(N - B)]
    for res in response:
        for i in range(N - B):
            resdata[i] += res[i]

    exists = []
    for res in resdata:
        exists.append(int(res, 2))
    ans = []
    for i in range(N):
        if i not in exists:
            ans.append(str(i))

    print(" ".join(ans), flush=True)
    print("My answer : ", " ".join(ans), file=stderr, flush=True)

    verdict = input()
    if verdict == "1":
        return True
    else:
        return False

t = int(input())
for case in range(1, t + 1):
    print("Test Case : ", case, file=stderr, flush=True)
    N, B, F = tuple(map(int, input().split(" ")))
    print(N, B, F, file=stderr, flush=True)
    if not solve(N, B, F):
      break
exit()
