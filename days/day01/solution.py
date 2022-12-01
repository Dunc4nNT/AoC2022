def get_calories_per_elf() -> list[int]:
    with open("input.txt", "r") as f:
        return [
            sum([int(x) for x in line.splitlines()]) for line in f.read().split("\n\n")
        ]


def part1() -> int:
    return max(get_calories_per_elf())


def part2() -> int:
    calories = get_calories_per_elf()
    calories.sort()

    return sum(calories[-3:])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
