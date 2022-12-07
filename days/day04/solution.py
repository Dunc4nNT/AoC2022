import re


def get_input() -> list[list[int]]:
    with open("input.txt") as f:
        pairs = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", f.read())
        return [
            [int(a_start), int(a_end), int(b_start), int(b_end)]
            for a_start, a_end, b_start, b_end in pairs
        ]


def part1(pairs: list[list[int]]) -> int:
    return len(
        [
            1
            for pair in pairs
            if pair[0] <= pair[2] <= pair[3] <= pair[1]
            or pair[2] <= pair[0] <= pair[1] <= pair[3]
        ]
    )


def part2(pairs: list[list[int]]) -> int:
    return len([1 for pair in pairs if pair[0] <= pair[3] and pair[2] <= pair[1]])


if __name__ == "__main__":
    data = get_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
