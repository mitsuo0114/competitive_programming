def solve(A, B):
    if A % 2 == 0 or B % 2 == 0:
        return "No"
    return "Yes"

if __name__ == "__main__":
    l = input()
    A, B = int(l.split()[0]),int(l.split()[1])
    print(solve(A, B))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(3, 1), "Yes")

    def test_2(self):
        self.assertEqual(solve(1, 2), "No")

    def test_3(self):
        self.assertEqual(solve(2, 2), "No")
