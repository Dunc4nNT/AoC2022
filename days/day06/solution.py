def get_input() -> str:
    with open("input.txt") as f:
        return f.readline()


def get_unique_str_index(data: str, size: int) -> int | None:
    unique_str: list[str] = []

    for i, char in enumerate(data):
        if len(unique_str) == size:
            return i

        if char in unique_str:
            unique_str = unique_str[unique_str.index(char) + 1 :]

        unique_str.append(char)

    return None


def part1(data: str) -> int | None:
    return get_unique_str_index(data, 4)


def part2(data: str) -> int | None:
    return get_unique_str_index(data, 14)


if __name__ == "__main__":
    data = get_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
