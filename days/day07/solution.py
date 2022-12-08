class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    parent: "Directory"

    def __init__(self, name: str) -> None:
        self.name = name
        self._dirs: list[Directory] = []
        self._files: list[File] = []

    def add_directory(self, dir: "Directory") -> None:
        self._dirs.append(dir)
        dir.parent = self

    def add_file(self, file: File) -> None:
        self._files.append(file)

    def get_directory(self, dir: str) -> "Directory":
        return next(_dir for _dir in self._dirs if _dir.name == dir)

    def get_all_directories_recursive(self) -> list["Directory"]:
        all_dirs = []

        for dir in self._dirs:
            all_dirs.extend(dir.get_all_directories_recursive())

        all_dirs.extend(self._dirs)

        return all_dirs

    def get_size(self) -> int:
        return sum(file.size for file in self._files) + sum(
            dir.get_size() for dir in self._dirs
        )


def get_root() -> Directory:
    with open("input.txt") as f:
        data = f.read().splitlines()

    root = Directory("/")
    cwd = root

    for line in data:
        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            dir = line.split("cd")[1].strip()

            match dir:
                case "/":
                    cwd = root
                case "..":
                    if cwd == root:
                        continue
                    cwd = cwd.parent
                case _:
                    cwd = cwd.get_directory(dir)
        elif line.startswith("dir"):
            dir = line.split()[1]
            dir = Directory(dir)
            cwd.add_directory(dir)
        else:
            size, file = line.split()
            file = File(file, int(size))
            cwd.add_file(file)

    return root


def part1(root: Directory) -> int:
    all_dirs = root.get_all_directories_recursive()
    max_size = 100000
    return sum(dir.get_size() for dir in all_dirs if dir.get_size() <= max_size)


def part2(root: Directory) -> int:
    all_dirs = root.get_all_directories_recursive()
    all_dirs.append(root)
    minimum_required_space = 30000000
    total_space = 70000000
    current_free_space = total_space - root.get_size()
    return min(
        dir.get_size()
        for dir in all_dirs
        if dir.get_size() >= minimum_required_space - current_free_space
    )


if __name__ == "__main__":
    root = get_root()
    print(f"Part 1: {part1(root)}")
    print(f"Part 2: {part2(root)}")
