
from math import ceil, sqrt
from operator import add
import timeit
from enum import Enum


"""
65  64  63  62  61  60  59  58  57
66  37  36  35  34  33  32  31  56
67  38  17  16  15  14  13  30  55
68  39  18   5   4   3  12  29  54
69  40  19   6   1   2  11  28  53
70  41  20   7   8   9  10  27  52
71  42  21  22  23  24  25  26  51
72  43  44  45  46  47  48  49  50
73  74  75  76  77  78  79  80  81  82
"""


def manhattan_distance(start, end):
    return sum(abs(e - s) for s, e in zip(start, end))


def square_size(index):
    return ceil(sqrt(index)) // 2 * 2 + 1


def square_layer(size):
    return ceil(size / 2)


def coord_add(c1, c2):
    return tuple(map(add, c1, c2))


def adjust(size, start, dest_index, final_index):

    x, y = start
    size -= 1  # coords start at 0
    distance = final_index - dest_index
    y += min(distance, size - 1)
    # first adjustment is offset by 1, as start isn't quite in the bottom right
    distance -= size - 1
    distance = max(distance, 0)
    x -= min(distance, size)
    distance -= size
    distance = max(distance, 0)
    y -= min(distance, size)
    distance -= size
    distance = max(distance, 0)
    x += min(distance, size)
    return x, y


def faster_coords(dest_index):
    size = square_size(dest_index)
    layer = square_layer(size)
    print("size {}".format(size))
    print("layer {}".format(layer))
    # e.g. square number 3, first index is 10. Square 4, first index is 26
    square_start = pow((size - 2), 2) + 1
    print("start square: {}".format(square_start))
    ss_coords = (size - layer), (layer - size + 1)
    print("ss_coords: {}".format(ss_coords))
    final = adjust(size, ss_coords, square_start, dest_index)

    return final


def brute_force(start_coords, dest_index):

    if dest_index == 1:
        return 0, 0

    size = 2  # travel size, rather than square dimension
    # Because of our earlier checks, we'll always start at 2
    x, y = start_coords
    distance = dest_index - 1
    while distance:
        # bump to next square_layer
        x += 1
        distance -= 1

        y += min(distance, size - 1)
        distance -= size - 1
        if distance < 0:
            break

        x -= min(distance, size)
        distance -= size
        if distance < 0:
            break

        y -= min(distance, size)
        distance -= size
        if distance < 0:
            break

        x += min(distance, size)
        distance -= size
        if distance < 0:
            break

        size += 2
    return x, y


def carry_data(dest_index):
    cheat_coords = None
    if dest_index == 1:
        c_md = 0
    elif dest_index <= 9:
        c_md = dest_index % 2 + 1
    else:
        cheat_coords = faster_coords(dest_index)
        c_md = manhattan_distance((0, 0), cheat_coords)

    brute_coords = brute_force((0, 0), dest_index)
    b_md = manhattan_distance((0, 0), brute_coords)
    # print("Brute force: {}, Cheat: {}".format(brute_coords, cheat_coords))

    print("{} ({}) is {} away, or possibly {}".format(dest_index, cheat_coords, b_md, c_md))


class Direction(Enum):
    up = 1
    right = 2
    down = 3
    left = 4


class Point(object):
    """docstring for Point."""

    def __init__(self, index, x, y, value=None):
        self.index = index
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return "Point {}: {},{}: {}".format(self.index, self.x, self.y, self.value)


def adjacent(p1, p2):
    if abs(p1.x - p2.x) > 1:
        return False
    if abs(p1.y - p2.y) > 1:
        return False
    return True


def stress_test(threshold):

    storage = [Point(1, 0, 0, 1)]

    x, y = 0, 0
    size = 1
    location = 1
    direction = Direction.right

    while storage[-1].value <= threshold:
        if direction == Direction.right:
            x += 1
            if x == size and y == -size:
                size += 1
            if x == size:
                direction = Direction.up
        elif direction == Direction.up:
            y += 1
            if y == size:
                direction = Direction.left
        elif direction == Direction.left:
            x -= 1
            if x == -size:
                direction = Direction.down
        elif direction == Direction.down:
            y -= 1
            if y == -size:
                direction = Direction.right
        location += 1

        newpoint = Point(location, x, y)
        value = 0
        for point in storage:
            if adjacent(point, newpoint):
                value += point.value
        newpoint.value = value
        storage.append(newpoint)
    print("Stress test found: {}".format(storage[-1].value))


if __name__ == '__main__':
    carry_data(1)
    carry_data(12)
    carry_data(23)
    carry_data(82)
    carry_data(1024)
    carry_data(312051)
    stress_test(312051)
