def fib(n):
    r5 = pow(5, 1/2)
    return  int (
            (1 / r5) *
            (
                pow((1 + r5) / 2, n)
                -
                pow((1 - r5) / 2, n)
            )
    )

f = [fib(k) for k in range(1, 40)]
for i in range(0, len(f) - 2):
    if f[i + 2] != f[i + 1] + f[i]:
        print(f"wrong {f[i + 2]} != {f[i + 1]} + {f[i]}")