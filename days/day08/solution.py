import math


def get_data() -> list[list[int]]:
    with open("input.txt", "r") as f:
        return [[int(i) for i in line.strip()] for line in f.readlines()]


def check_direction(tree, other_trees: list[int]) -> tuple[bool, int]:
    count = 0
    for other_tree in other_trees:
        count += 1
        if other_tree >= tree:
            return True, count
    return False, count


def get_tree(ix, iy, data) -> tuple[bool, int]:
    directions = (
        [data[jy][ix] for jy in reversed(range(0, iy))],
        data[iy][ix + 1 :],
        [data[jy][ix] for jy in range(iy + 1, len(data))],
        list(reversed(data[iy][:ix])),
    )
    results = [check_direction(data[iy][ix], direction) for direction in directions]

    return (
        all(result[0] for result in results),
        math.prod(result[1] for result in results),
    )


def get_all_trees(data) -> list[tuple[bool, int]]:
    return [
        get_tree(ix, iy, data)
        for ix in range(len(data[0]))
        for iy in range(len(data))
        if iy != 0 and iy != len(data) - 1 and ix != 0 and ix != len(data[0]) - 1
    ]


def part1(data: list[list[int]]) -> int:
    return len(data) * len(data[0]) - sum([hidden for hidden, _ in get_all_trees(data)])


def part2(data) -> int:
    return max([tree_view for _, tree_view in get_all_trees(data)])


if __name__ == "__main__":
    data = get_data()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
