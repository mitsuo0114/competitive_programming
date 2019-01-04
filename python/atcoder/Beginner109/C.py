

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def solve(N, X, cities):
    dists = [abs(city - X) for city in cities]
    ans = min(dists)
    for d in dists:
        if d % ans == 0:
            continue
        else:
            ans = gcd(ans, d % ans)
    return ans

if __name__ == "__main__":
    l = input()
    N, X = int(l.split()[0]),int(l.split()[1])
    cities = [int(c) for c in input().split()]
    print(solve(N, X, cities))


import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(3, 3, [int(c) for c in "1 7 11".split()]),2)

    def test_2(self):
        self.assertEqual(solve(3, 81, [int(c) for c in "33 105 57".split()]),24)
