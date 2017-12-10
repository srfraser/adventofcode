import sys
from collections import defaultdict
import operator

"""
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


REGISTERS = defaultdict(int)
HIGHEST = 0


def part1(line):
    """Not bothering with a proper parser, because tired."""
    register, operation, value, _, *rest = line.split()
    global HIGHEST
    cond_reg = "REGISTERS['{}']".format(rest[0])
    rest[0] = cond_reg
    condition = " ".join(rest)
    # print(condition, eval(condition))
    if eval(condition):
        if operation == 'inc':
            REGISTERS[register] += int(value)
        else:
            REGISTERS[register] -= int(value)
        HIGHEST = max(HIGHEST, REGISTERS[register])


def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            part1(line)

    m = max(REGISTERS.items(), key=operator.itemgetter(1))[0]
    print("Maximum value at the end is in {}: {}".format(m, REGISTERS[m]))
    print("Highest value during operation was {}".format(HIGHEST))


if __name__ == '__main__':
    main()
