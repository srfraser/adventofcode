
import sys
from collections import Counter

def match(data):
    s1, s2 = list(data)
    if s1.lower() == s2.lower() and s1 != s2:
        return True
    return False


def reduce(data):
    while True:
        pairs = ["".join(f) for f in zip(data, data[1:])]
        for pair in pairs:
            if match(pair):
                data = data.replace(pair, '')
                break
        else:
            break
    return data


def part1(input_file):
    with open(input_file) as f:
        data = f.read().strip('\n')

    # data = 'dabAcCaCBAcCcaDA'
    data = reduce(data)
    print("Part 1: ", len(data))


def part2(input_file):
    with open(input_file) as f:
        data = f.read().strip('\n')

    counter = Counter(list([d.lower() for d in data]))

    results = dict()
    for removal in counter.keys():
        data2 = data.replace(removal, '').replace(removal.upper(), '')
        data2 = reduce(data2)
        print("Removing", removal, "gives", len(data2))
        results[removal] = len(data2)

    print("Part 2: ", min(results, key=results.get))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    part1(filename)
    part2(filename)
