from pathlib import Path

if __name__ == "__main__":
    for day in range(1, 26):
        day_dir = Path(f"days/day{day:02}")

        if day_dir.exists():
            continue

        day_dir.mkdir(parents=True, exist_ok=True)

        Path(day_dir / "input.txt").touch()
        Path(day_dir / "solution.py").touch()
        Path(day_dir / "test.txt").touch()
