from string import ascii_letters


def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def part1(rucksacks: list[str]) -> int:
    duplicates = [
        set(rucksack[: len(rucksack) // 2]).intersection(
            set(rucksack[len(rucksack) // 2 :])
        )
        for rucksack in rucksacks
    ]

    return sum(
        [
            ascii_letters.index(duplicate) + 1
            for duplicate_set in duplicates
            for duplicate in duplicate_set
        ]
    )


def part2(rucksacks: list[str]) -> int:
    rucksacks_by_group = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

    return sum(
        [
            ascii_letters.index(
                set(group[0]).intersection(set(group[1]), set(group[2])).pop()
            )
            + 1
            for group in rucksacks_by_group
        ]
    )


if __name__ == "__main__":
    data = get_input()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
