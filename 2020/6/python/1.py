import os
from pathlib import Path


def part1(data):
    return sum(len(set(entry.replace("\n", ""))) for entry in data.split("\n\n"))


def part2(data):
    total = 0
    for entry in data.split("\n\n"):
        people = len(entry.splitlines())
        total += len(
            [
                value
                for value in set(entry.replace("\n", ""))
                if entry.count(value) == people
            ]
        )
    return total


if __name__ == "__main__":
    test_filename = Path(os.path.dirname(__file__)) / "../test_input"
    test_data = test_filename.read_text()

    filename = Path(os.path.dirname(__file__)) / "../input"
    data = filename.read_text()

    print("Test Part 1: ", part1(test_data))
    print("Part 1: ", part1(data))
    print("Test Part 2: ", part2(test_data))
    print("Part 2: ", part2(data))
