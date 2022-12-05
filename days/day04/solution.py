import re
from typing import NamedTuple


class Pair(NamedTuple):
    a_start: int
    a_end: int
    b_start: int
    b_end: int


def get_input():
    pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    pairs: list[Pair] = []

    with open("input.txt") as f:
        for line in f.readlines():
            result = re.search(pattern, line)
            if result:
                a_start, a_end, b_start, b_end = result.groups()
                pairs.append(Pair(int(a_start), int(a_end), int(b_start), int(b_end)))

    return pairs


def part1() -> int:
    pairs = get_input()
    count = 0

    for pair in pairs:
        if (
            pair.a_start <= pair.b_start
            and pair.b_end <= pair.a_end
            or pair.b_start <= pair.a_start
            and pair.a_end <= pair.b_end
        ):
            count += 1

    return count


def part2() -> int:
    pairs = get_input()
    count = 0

    for pair in pairs:
        if pair.a_start <= pair.b_end and pair.b_start <= pair.a_end:
            count += 1

    return count


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
