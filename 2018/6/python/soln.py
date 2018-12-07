
import sys
from collections import Counter


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


def part1(input_file):

    test_input = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]

    data = list()
    with open(input_file) as f:
        for line in f:
            a, b = [int(i) for i in line.split(',')]
            data.append((a, b))

    max_x = max(i[0] for i in data) + 1
    max_y = max(i[1] for i in data) + 1
    coords = dict()
    for x in range(max_x):
        for y in range(max_y):
            coords[(x, y)] = dict()
            for point in data:
                coords[(x, y)][point] = manhattan_distance(x, y, point[0], point[1])

    for coord in coords:
        minimum = min(coords[coord].values())
        shared = [c for c in coords[coord] if coords[coord][c] == minimum]
        if len(shared) > 1:
            coords[coord] = None
        else:
            coords[coord] = shared[0]

    # remove borders
    removals = set([coords[coord] for coord in coords if (
        coord[0] == 0 or coord[1] == 0 or coord[0] == max_x-1 or coord[1] == max_y-1)])
    coords = {coord: coords[coord] for coord in coords if coords[coord] not in removals}

    c = Counter(coords.values())
    print(c.most_common(1))


def part2(input_file):
    data = list()
    with open(input_file) as f:
        for line in f:
            a, b = [int(i) for i in line.split(',')]
            data.append((a, b))

    max_x = max(i[0] for i in data) + 1
    max_y = max(i[1] for i in data) + 1
    min_x = min(i[0] for i in data)
    min_y = min(i[1] for i in data)

    coords = dict()
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            coords[(x, y)] = 0
            for point in data:
                coords[(x, y)] += manhattan_distance(x, y, point[0], point[1])

    results = [c for c in coords if coords[c] < 10000]
    print("Part 2", len(results))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    part1(filename)
    part2(filename)
