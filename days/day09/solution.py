from time import perf_counter


def get_data() -> list[tuple[str, int]]:
    with open("input.txt", "r") as f:
        return [
            (line[0], int(line[1])) for line in [line.split() for line in f.readlines()]
        ]


def get_tail_move(tail_coords, head_coords) -> tuple[int, int]:
    dx = head_coords[0] - tail_coords[0]
    dy = head_coords[1] - tail_coords[1]

    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail_coords

    if dx == 0:
        return (tail_coords[0], tail_coords[1] + 1 if dy > 0 else tail_coords[1] - 1)
    elif dy == 0:
        return (tail_coords[0] + 1 if dx > 0 else tail_coords[0] - 1, tail_coords[1])
    else:
        return (
            tail_coords[0] + 1 if dx > 0 else tail_coords[0] - 1,
            tail_coords[1] + 1 if dy > 0 else tail_coords[1] - 1,
        )


def solve(data: list[tuple[str, int]], n) -> int:
    possible_moves: dict[str, tuple[int, int]] = {
        "U": (0, 1),
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0),
    }
    rope: list[tuple[int, int]] = [(0, 0) for _ in range(n + 1)]
    visited: list[tuple[int, int]] = [rope[0]]

    for instruction, amount in data:
        for _ in range(amount):
            rope[0] = (
                rope[0][0] + possible_moves[instruction][0],
                rope[0][1] + possible_moves[instruction][1],
            )

            for i in range(1, len(rope)):
                rope[i] = get_tail_move(rope[i], rope[i - 1])
            visited.append(rope[-1])

    return len(set(visited))


if __name__ == "__main__":
    data = get_data()

    start1 = perf_counter()
    solution1 = solve(data, 1)
    stop1 = perf_counter()

    print(f"Part 1: {solution1} ({round((stop1 - start1) * 1000, 3)}ms)")

    start2 = perf_counter()
    solution2 = solve(data, 9)
    stop2 = perf_counter()

    print(f"Part 2: {solution2} ({round((stop2 - start2) * 1000, 3)}ms)")
