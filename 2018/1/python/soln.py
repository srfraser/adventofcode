
import sys
import itertools


def part1(input_file):
    frequency = 0
    with open(input_file) as f:
        for line in f:
            frequency += int(line)

    print(frequency)


def part2(input_file):
    frequency = 0

    with open(input_file) as f:
        modifiers = [int(line) for line in f]

    frequencies_seen = set()
    frequencies_seen.add(frequency)

    for modifier in itertools.cycle(modifiers):
        frequency += modifier
        if frequency in frequencies_seen:
            print("Duplicate", frequency)
            break
        frequencies_seen.add(frequency)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')

    part1(filename)
    part2(filename)
