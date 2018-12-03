
import sys
from collections import defaultdict

FABRIC_SIZE = 1000  # square


def empty_fabric():
    return [[0]*FABRIC_SIZE for _ in range(FABRIC_SIZE)]

    pass


def line_to_claim_id(line):
    return line.split()[0].replace('#', '')


def line_to_coords_list(line):
    """#1 @ 53,238: 26x24 -> ... """
    start_x, start_y = [int(i) for i in line.split()[2].replace(':', '').split(',')]
    size_x, size_y = [int(i) for i in line.split()[3].split('x')]
    for x in range(start_x, start_x + size_x):
        for y in range(start_y, start_y + size_y):
            yield (x, y)


def part1(input_file):
    fabric = defaultdict(int)

    with open(input_file) as f:
        for line in f:
            for coord in line_to_coords_list(line):
                fabric[coord] += 1

    overlaps = len([coord for coord in fabric if fabric[coord] > 1])
    print("Part 1: ", overlaps)


def part2(input_file):
    fabric = defaultdict(list)

    all_claims = set()
    with open(input_file) as f:
        for line in f:
            claim_id = line_to_claim_id(line)
            all_claims.add(claim_id)
            for coord in line_to_coords_list(line):
                fabric[coord].append(claim_id)

    claims_with_overlaps = set()
    for coord in fabric:
        if len(fabric[coord]) == 1:
            continue
        for claim_id in fabric[coord]:
            claims_with_overlaps.add(claim_id)

    print("Part 2", all_claims-claims_with_overlaps)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    part1(filename)
    part2(filename)
