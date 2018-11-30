
import sys


class Scanner(object):
    """docstring for Scanner."""

    def __init__(self, bound):
        self.location = 0
        self.direction = 'down'
        self.bound = bound - 1

    def __repr__(self):
        return "Scanner at {} going {}".format(self.location, self.direction)

    def tick(self):
        if self.location >= self.bound:
            self.direction = 'up'
        elif self.location <= 0:
            self.direction = 'down'

        if self.direction == 'up':
            self.location -= 1
        else:
            self.location += 1


def calc_severity(layer, depth):
    return layer * depth


def part1(firewall, delay=0):
    current_layer = -1
    severity = 0
    scanner_locs = {i: Scanner(bound=b) for i, b in firewall.items()}
    count = 0

    while current_layer <= max(firewall.keys()):
        if count >= delay:
            current_layer += 1
        else:
            count += 1

        if current_layer in scanner_locs:
            if scanner_locs[current_layer].location == 0:
                severity += calc_severity(current_layer, firewall[current_layer])
        for scanner in scanner_locs:
            scanner_locs[scanner].tick()

    return severity


def part2(firewall):
    """
    0 1 - 2 steps
    0 1 2 - 4 steps
    0 1 2 3 - 6 steps
    0 1 2 3 4 - 8 steps
    0 1 2 3 4 5 - 10 steps
    0 1 2 3 4 5 6 - 12 steps

    steps between zeroes = (len()-1) * 2
    let this be stepdiff

    So if any of these are layer 0, you want to wait any number that isn't
    divisible by stepdiff. e.g waiting 0,2,4,6 for [0,1] is fatal.

    if it's layer 1 then there's an offset. for layer 1 to be 'layer 0' for
    the calculation above, we've taken delay+layers to get there.

    So for any layer, we are ok as long as (delay+current_layer)%((depth-1)*2) is not 0
    """
    delay = -1
    caught = True

    while caught:
        delay += 1
        # Slow
        # caught = any([((delay + layer) % ((firewall[layer] - 1) * 2))
        #              == 0 for layer in firewall.keys()])
        for layer in firewall.keys():
            if ((delay + layer) % ((firewall[layer] - 1) * 2)) == 0:
                break
        else:
            return delay


def calc_severity_quicker(firewall, delay):
    severity = 0
    for layer in firewall.keys():
        if ((delay + layer) % ((firewall[layer] - 1) * 2)) == 0:
            severity += layer * firewall[layer]
    return severity


def main():
    firewall = dict()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            layer, depth = line.split(': ')
            firewall[int(layer)] = int(depth)

    severity = part1(firewall)
    print("Part 1 severity is {}".format(severity))
    severity = calc_severity_quicker(firewall, 0)
    print("Part 1 severity double check is {}".format(severity))
    # part2(firewall)
    delay = part2(firewall)
    print("part 2 delay is {}".format(delay))


if __name__ == '__main__':
    main()
