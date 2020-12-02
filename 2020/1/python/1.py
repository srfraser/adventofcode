import os
from pathlib import Path
from itertools import combinations
from functools import reduce

test_data = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def part1(data, num_factors=2, target=2020):
    for values in combinations(sorted(data), num_factors):
        if sum(values) == target:
            return reduce(lambda x, y: x * y, values)


if __name__ == "__main__":
    filename = Path(os.path.dirname(__file__)) / "../input"
    with filename.open() as f:
        part1_data = [int(i) for i in f]

    assert part1(test_data, target=2020) == 514579
    print("Part 1: ", part1(part1_data, target=2020))
    print("Part 2: ", part1(part1_data, target=2020, num_factors=3))
