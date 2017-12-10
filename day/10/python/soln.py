import sys
import pytest
from operator import xor
from functools import reduce


@pytest.mark.parametrize('circle,position,length,expected', (
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 2, [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 2, [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6, [5, 1, 2, 3, 4, 0, 9, 8, 7, 6]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 10, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
))
def test_reverse(circle, position, length, expected):
    assert reverse(circle, position, length) == expected


def reverse(circle, position, length):
    """Reverse circle[position:length], wrapping to the start if required."""
    if length > len(circle):
        raise ValueError("Unable to reverse %d elements", length)
    temp = (circle[position:position + length] +
            circle[0:max((position + length) - len(circle), 0)])[::-1]

    circle[position:min(len(circle), position + length)] = temp[0:len(circle) - position]

    circle[0:max(position + length - len(circle), 0)] = temp[len(circle) - position:]
    return circle


def part1(data):
    current_position = 0
    skip_size = 0
    circle = list(range(256))
    for length in data:
        circle = reverse(circle, current_position, length)
        current_position = (current_position + length + skip_size) % len(circle)
        skip_size += 1

    print("circle[0] * circle[1] = {} * {} = {}".format(circle[0],
                                                        circle[1], circle[0] * circle[1]))


@pytest.mark.parametrize("data,expected", (
    ("", 'a2582a3a0e66e6e86e3812dcb672a272'),
    ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
    ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
    ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e")
))
def test_part2(data, expected):
    assert part2(data) == expected


def part2(raw_data):
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

    return "".join(["{0:0{1}x}".format(d, 2) for d in dhash])


def main():
    with open(sys.argv[1], 'r') as f:
        raw_data = f.readline()
    part1_data = [int(i) for i in raw_data.split(',')]
    part1(part1_data)

    result = part2(raw_data.strip())
    print("Knot hash: {}".format(result))


if __name__ == '__main__':
    main()
