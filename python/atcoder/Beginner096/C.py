def solve(H, W, field):
    for hi, row in enumerate(field):
        for wi, cel in enumerate(row):
            if cel != "#":
                continue
            if any([field[hi + dh][dw + wi] == "#"
                    for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    if 0 <= hi + dh < H and 0 <= dw + wi < W]):
                pass
            else:
                return "No"
    return "Yes"


assert (solve(2, 2, ["..", ".."]) == "Yes")
assert (solve(2, 3, ["...", "..."]) == "Yes")
assert (solve(2, 3, [".#.", "..."]) == "No")
assert (solve(2, 3, ["##.", "..."]) == "Yes")
assert (solve(2, 3, ["..#", "..."]) == "No")
assert (solve(2, 3, ["..,", "..#"]) == "No")
assert (solve(3, 3, ['.#.', '###', '.#.']) == "Yes")
assert (solve(5, 5, ['#.#.#', '.#.#.', '#.#.#', '.#.#.', '#.#.#']) == "No")
assert (solve(11, 11,
              ['...#####...', '.##.....##.', '#..##.##..#', '#..##.##..#', '#.........#', '#...###...#', '.#########.',
               '.#.#.#.#.#.', '##.#.#.#.##', '..##.#.##..', '.##..#..##.']
              ) == "Yes")

if __name__ == "__main__":
    H, W = tuple(map(int, input().split(" ")))
    field = [input() for _ in range(H)]
    print(solve(H, W, field))
