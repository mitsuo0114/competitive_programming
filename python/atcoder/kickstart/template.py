sample_input = """
"""

small_input = """
"""

large_input= """
"""

from collections import Counter
def solve(A, B):
    return c


data = large_input
As = data.splitlines()[3::3]
Bs = data.splitlines()[4::3]
with open("out/2018F-A.large.txt", "w") as f:
    for i, (A, B) in enumerate(zip(As, Bs)):
        t = "Case #%d: %d" %(i+1, solve(A, B))
        print(t)
        f.write(t)
        f.write("\n")




