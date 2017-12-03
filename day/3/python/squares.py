
from math import ceil, sqrt
from operator import add
import timeit

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
    # e.g. square number 3, first index is 10. Square 4, first index is 26
    square_start = pow((size - 2), 2) + 1
    ss_coords = (size - layer), (layer - size + 1)
    final = adjust(size, ss_coords, square_start, dest_index)
    return final


def brute_force(dest_index):

    if dest_index == 1:
        return 0, 0

    size = 2  # travel size, rather than square dimension
    # Because of our earlier checks, we'll always start at 2
    x, y = 0, 0
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

    brute_coords = brute_force(dest_index)
    b_md = manhattan_distance((0, 0), brute_coords)
    # print("Brute force: {}, Cheat: {}".format(brute_coords, cheat_coords))

    print("{} is {} away, or possibly {}".format(dest_index, b_md, c_md))

    def wrap_cheat():
        faster_coords(dest_index)

    cheat_timing = timeit.timeit(wrap_cheat)
    print("Shortcut elapsed time: {}".format(cheat_timing))

    def wrap_brute():
        brute_force(dest_index)

    brute_timing = timeit.timeit(wrap_brute)
    print("Brute force elapsed time: {}".format(brute_timing))
    print("")


if __name__ == '__main__':
    carry_data(1)
    carry_data(12)
    carry_data(23)
    carry_data(82)
    carry_data(1024)
    carry_data(312051)
