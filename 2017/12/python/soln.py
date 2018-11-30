
import sys


def scan(network, start):
    seen = list()
    to_scan = [start]
    while to_scan:
        node = to_scan.pop(0)
        seen.append(node)
        to_scan.extend([n for n in network[node] if n not in seen and n not in to_scan])
    for n in seen:
        del network[n]
    return len(seen)


def main():
    network = dict()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            node, _, *rest = line.split()
            network[node] = [r.strip(',') for r in rest]

    p2_network = dict(network)

    seen = scan(network, '0')
    print("Part 1 visited {} nodes".format(seen))

    groups = 0
    while p2_network:
        start = list(p2_network.keys())[0]
        seen = scan(p2_network, start)
        groups += 1
    print("Found {} groups".format(groups))


if __name__ == '__main__':
    main()
