import os
from pathlib import Path


def part1(data):
    valid = 0
    for line in data:
        policy, password = line.split(": ")
        values, letter = policy.split()
        low, high = [int(i) for i in values.split("-")]
        if low <= password.count(letter) <= high:
            valid += 1
    return valid


def part2(data):
    valid = 0
    for line in data:
        policy, password = line.split(": ")
        values, letter = policy.split()
        low, high = [int(i) - 1 for i in values.split("-")]
        if password[low] == password[high]:
            continue
        if password[low] == letter or password[high] == letter:
            valid += 1

    return valid


if __name__ == "__main__":
    test_filename = Path(os.path.dirname(__file__)) / "../test_input"
    test_data = test_filename.read_text().splitlines()

    filename = Path(os.path.dirname(__file__)) / "../input"
    data = filename.read_text().splitlines()

    print("Test Part 1: ", part1(test_data))
    print("Part 1: ", part1(data))
    print("Test Part 2: ", part2(test_data))
    print("Part 2: ", part2(data))