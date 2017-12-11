"""
https://www.redblobgames.com/grids/hexagons/
"""

import sys
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y', 'z'])

direction_map = {
    'n': Coord(x=0, y=1, z=-1),
    'ne': Coord(x=1, y=0, z=-1),
    'se': Coord(x=1, y=-1, z=0),
    's': Coord(x=0, y=-1, z=1),
    'sw': Coord(x=-1, y=0, z=1),
    'nw': Coord(x=-1, y=1, z=0),
}


def cube_distance(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2


def move(start, direction):
    return Coord(
        x=start.x + direction_map[direction].x,
        y=start.y + direction_map[direction].y,
        z=start.z + direction_map[direction].z)


def part1(directions):
    current = Coord(x=0, y=0, z=0)
    start = Coord(x=0, y=0, z=0)
    distances = list()
    print(current)
    for direction in directions:
        current = move(current, direction)
        distances.append(cube_distance(start, current))
    print("Position {} is {} steps away".format(current, cube_distance(start, current)))
    print("Furthest point from the start was {} steps away".format(max(distances)))


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readline()
        data = data.rstrip('\n')

    directions = data.split(',')
    part1(directions)


if __name__ == '__main__':
    main()
