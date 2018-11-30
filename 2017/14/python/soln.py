from operator import xor
from functools import reduce


def reverse(circle, position, length):
    """Stolen from Day 10."""
    rotate(circle, -position)
    circle[0:length] = circle[0:length][::-1]
    rotate(circle, position)
    return circle


def rotate(lst, x):
    """Stolen from Day 10."""
    lst[:] = lst[-x:] + lst[:-x]


def knothash(raw_data):
    """Stolen from Day 10."""
    data = [ord(c) for c in raw_data]

    # Arbitrary question data
    data.extend([17, 31, 73, 47, 23])
    current_position = 0
    skip_size = 0
    circle = list(range(256))
    for _ in range(64):
        for length in data:
            circle = reverse(circle, current_position, length)
            current_position = (current_position + length + skip_size) % len(circle)
            skip_size += 1

    # Create dense hash
    dhash = list()
    for chunk in range(0, 255, 16):
        dhash.append(reduce(xor, circle[chunk:chunk + 16]))

    return "".join([format(d, '08b') for d in dhash])


def part1():
    data = 'hfdlxzhv'
    counting_zeroes = 0
    grid = list()
    for i in range(128):
        result = knothash("{}-{}".format(data, i))
        grid.append(result)
        counting_zeroes += result.count('1')
    print("Zeroes: {}".format(counting_zeroes))
    return grid


def find_starting_one(grid):
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == '1':
                return x, y
    return None, None


def adjacent(x, y, gridsize):
    if x < gridsize:
        yield x + 1, y
    if y < gridsize:
        yield x, y + 1
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1


def showgrid(grid):
    for y in grid:
        print("".join(y))


def part2(grid):
    """Count the regions."""
    counted_regions = 0
    gridsize = len(grid) - 1  # Assume square
    x, y = 0, 0

    for y, row in enumerate(grid):
        grid[y] = list(row)

    seen = list()
    showgrid(grid)

    while True:
        to_scan = list()
        x, y = find_starting_one(grid)
        if x is None or y is None:
            break
        to_scan.append((x, y))

        while to_scan:
            x, y = to_scan.pop(0)
            seen.append((x, y))
            grid[y][x] = '0'
            for adj_x, adj_y in adjacent(x, y, gridsize):
                if grid[adj_y][adj_x] == '1' and (adj_x, adj_y) not in seen and (adj_x, adj_y) not in to_scan:
                    to_scan.append((adj_x, adj_y))
        counted_regions += 1
    print("")
    showgrid(grid)
    return counted_regions


def main():
    grid = part1()
    regions = part2(grid)
    print("Found {} regions".format(regions))


if __name__ == '__main__':
    main()
