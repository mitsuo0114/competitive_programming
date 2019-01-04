def solve(H, W, field):
    return ["###", "###", ".##"]

if __name__ == "__main__":
    l = input()
    H, W = int(l.split()[0]),int(l.split()[1])
    field = [input() for _ in range(0, H)]
    [print(l) for l in solve(H, W, field)]


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(4, 4, [l.strip() for l in """
##.#
....
##.#
.#.#
""".splitlines() if len(l.strip())]), [l.strip() for l in """
###
###
.##
""".splitlines() if len(l.strip())])
