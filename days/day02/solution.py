from collections import Counter


def get_input() -> Counter[str]:
    with open("input.txt", "r") as f:
        return Counter([line.strip() for line in f.readlines()])


def part1(data: Counter[str]) -> int:
    SHAPE_SCORES = {"X": 1, "Y": 2, "Z": 3}
    WINNING_CASES = {"A Y", "B Z", "C X"}
    DRAW_CASES = {"A X", "B Y", "C Z"}
    score = 0

    for k, v in data.items():
        score += SHAPE_SCORES[k[-1]] * v
        if k in DRAW_CASES:
            score += 3 * v
        elif k in WINNING_CASES:
            score += 6 * v

    return score


def part2(data: Counter[str]) -> int:
    SHAPE_SCORES = {"A": 1, "B": 2, "C": 3}
    WINNING_CASES = {"A": "B", "B": "C", "C": "A"}
    LOSING_CASES = {v: k for k, v in WINNING_CASES.items()}
    score = 0

    for k, v in data.items():
        if k[-1] == "X":
            score += SHAPE_SCORES[LOSING_CASES[k[0]]] * v
        elif k[-1] == "Y":
            score += v * (SHAPE_SCORES[k[0]] + 3)
        else:
            score += v * (SHAPE_SCORES[WINNING_CASES[k[0]]] + 6)

    return score


if __name__ == "__main__":
    data = get_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
