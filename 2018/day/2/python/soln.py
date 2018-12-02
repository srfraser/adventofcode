
import sys
from collections import Counter
from itertools import combinations


def exactly(data, count=2):
    if [k for k, c in Counter(data).items() if c == count]:
        return 1
    return 0


def part1(input_file):
    twos = 0
    threes = 0
    with open(input_file) as f:
        for line in f:
            twos += exactly(line, count=2)
            threes += exactly(line, count=3)
    print("Checksum", twos * threes)


def part2(input_file):
    with open(input_file) as f:
        data = [line.strip() for line in f]

    for s1, s2 in combinations(data, 2):
        pos = match(s1, s2)
        if pos:
            print(s1, s2, pos)
            print("{}{}".format(s1[:pos], s1[pos+1:]))


def match(s1, s2):
    pos = None

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != None:
                return None
            else:
                pos = i

    return pos


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    part1(filename)
    part2(filename)
