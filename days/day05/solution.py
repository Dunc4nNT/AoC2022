import re
from collections import defaultdict


def get_input() -> tuple[defaultdict[int, list[str]], list[list[int]]]:
    with open("input.txt") as f:
        stacks_input, moves_input = f.read().split("\n\n")

    vertical_stacks = [stack[1::4] for stack in stacks_input.splitlines()[:-1]]

    stacks = defaultdict(list)
    for vertical_stack in vertical_stacks:
        for i, crate in enumerate(vertical_stack):
            if crate != " ":
                stacks[i].insert(0, crate)

    moves = re.findall(r"move (\d+) from (\d+) to (\d+)", moves_input)
    moves = [[int(amount), int(from_) - 1, int(to) - 1] for amount, from_, to in moves]

    return stacks, moves


def part1() -> str:
    stacks, moves = get_input()

    for amount, from_, to in moves:
        for _ in range(amount):
            stacks[to].append(stacks[from_].pop())

    return "".join(stacks[i][-1] for i in range(len(stacks)))


def part2() -> str:
    stacks, moves = get_input()

    for amount, from_, to in moves:
        stacks[to].extend(stacks[from_][-amount:])
        del stacks[from_][-amount:]

    return "".join(stacks[i][-1] for i in range(len(stacks)))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
