def solve(x1, y1, x2, y2):

    x3, y3 = int(x2 - (y2 - y1)), int(y2 + (x2 - x1))
    x4, y4 = int(x1 - (y2 - y1)), int(y1 + (x2 - x1))

    return " ".join(str(i) for i in [x3, y3, x4, y4])

if __name__ == "__main__":
    l = input()
    x1, y1, x2, y2 = int(l.split()[0]),int(l.split()[1]), int(l.split()[2]), int(l.split()[3])
    print(solve(x1, y1, x2, y2))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(0,0,0,1), "-1 1 -1 0")

    def test_2(self):
        self.assertEqual(solve(2,3,6,6), "3 10 -1 7")

    def test_3(self):
        self.assertEqual(solve(31, -41, -59, 26), "-126 -64 -36 -131")
