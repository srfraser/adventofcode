
import sys


def get_offsets(filename):
    with open(filename, 'r') as f:
        return [int(i) for i in f.readlines()]


def part1():
    jump_offsets = get_offsets(sys.argv[1])

    max_index = len(jump_offsets)
    current_index = 0

    steps = 0

    while 0 <= current_index < max_index:
        prev_index = current_index
        current_index += jump_offsets[current_index]
        jump_offsets[prev_index] += 1
        steps += 1

    print("Part 1 steps: {}".format(steps))


def part2():
    jump_offsets = get_offsets(sys.argv[1])

    max_index = len(jump_offsets)
    current_index = 0

    steps = 0

    while 0 <= current_index < max_index:
        prev_index = current_index
        current_index += jump_offsets[current_index]
        print("{}({}) to {}".format(prev_index, jump_offsets[prev_index], current_index))
        if jump_offsets[prev_index] >= 3:
            jump_offsets[prev_index] -= 1
        else:
            jump_offsets[prev_index] += 1
        steps += 1

    print("Part 2 steps: {}".format(steps))



if __name__ == '__main__':
    part1()
    part2()
