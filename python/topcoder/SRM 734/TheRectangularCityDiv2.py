# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TheRectangularCityDiv2:

    def search(self, city, start):
        candidate = [start]
        final = start
        visited = set()
        waycountmap = {}
        while(len(candidate)):
            (sx, sy) = candidate.pop()
            final = (sx, sy)
            visited.add(final)
            count = 0
            for (xi, yi) in [(sx + 1, sy), (sx - 1, sy),
                             (sx, sy + 1), (sx, sy - 1)]:
                if 0 <= xi < len(city[0]) and 0 <= yi < len(city):
                    if city[yi][xi] == ".":
                        count += 1
                    if city[yi][xi] == "." and (xi, yi) not in visited:
                        candidate.append( (xi, yi) )
                waycountmap[(sx, sy)] = count
        return final, len(visited), waycountmap

    def find(self, city):
        candidate = []
        opencount = 0
        for x in range(0, len(city[0])):
            for y in range(0, len(city)):
                if 0 <= x < len(city[0]) and 0 <= y < len(city):
                    if city[y][x] == ".":
                        opencount += 1

                if x == 0 or y == 0 or x == len(city[0]) -1 or y == len(city) - 1:
                    if city[y][x] == ".":
                        candidate.append((x, y))
        endpoint_list = []
        visited_count_list = []
        candidate_list = []
        waycountmap_list = {}
        while(len(candidate)):
            (x, y) = candidate.pop()
            endpoint, visited_count, waycountmap = self.search(city, (x, y))
            endpoint_list.append(endpoint)
            visited_count_list.append(visited_count)
            candidate_list.append((x, y))
            waycountmap_list[(x, y)] = waycountmap

        # failed
        if opencount != min(visited_count_list):
            return 0

        # loop
        endpoint = endpoint_list[0]
        (x, y) = candidate_list[0]
        count_map = waycountmap_list[(x, y)]
        odd_count = len([c for c in count_map.values() if c % 2 == 1])

        if odd_count == 0:
            return 2 * opencount

        # 一筆書き
        self.oddcount_min = min(count_map.values())
        if self.oddcount_min == 1:
            return 2
        else:
            three_count = len([c for c in count_map.values() if c == 3])
            two_count = len([c for c in count_map.values() if c == 2])
            four_count = len([c for c in count_map.values() if c == 4])
            return (three_count * 2 * three_count) + two_count * 2 * 2 * four_count
        return 0

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(city, __expected):
    startTime = time.time()
    instance = TheRectangularCityDiv2()
    exception = None
    try:
        __result = instance.find(city);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("TheRectangularCityDiv2 (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TheRectangularCityDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            city = []
            for i in range(0, int(f.readline())):
                city.append(f.readline().rstrip())
            city = tuple(city)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(city, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1535203710
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
