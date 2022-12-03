from string import ascii_letters


def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def part1() -> int:
    rucksacks = get_input()

    total = 0

    for rucksack in rucksacks:
        middle = len(rucksack) // 2
        duplicates = set(rucksack[:middle]).intersection(set(rucksack[middle:]))

        for duplicate in duplicates:
            total += ascii_letters.index(duplicate) + 1

    return total


def part2() -> int:
    rucksacks = get_input()
    rucksacks_by_group = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

    total = 0

    for group in rucksacks_by_group:
        total += (
            ascii_letters.index(
                set(group[0]).intersection(set(group[1]), set(group[2])).pop()
            )
            + 1
        )

    return total


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
