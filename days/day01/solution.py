def get_calories_per_elf() -> list[int]:
    with open("input.txt", "r") as f:
        return sorted(
            [
                sum([int(x) for x in line.splitlines()])
                for line in f.read().split("\n\n")
            ]
        )


def part1(calories: list[int]) -> int:
    return max(calories)


def part2(calories: list[int]) -> int:
    return sum(calories[-3:])


if __name__ == "__main__":
    data = get_calories_per_elf()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
