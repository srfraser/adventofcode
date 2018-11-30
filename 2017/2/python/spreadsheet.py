import itertools


def checksum(filename):
    checksum = 0
    with open(filename, 'r') as f:
        for line in f:
            data = [int(i) for i in line.split()]
            checksum += max(data) - min(data)
    return checksum


def evenly_divisible(filename):
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            data = [int(i) for i in line.split()]
            for subset in itertools.combinations(data, 2):
                quotient, remainder = divmod(max(subset), min(subset))
                if remainder == 0:
                    total += quotient
    return total


if __name__ == '__main__':
    import sys
    print("Checksum is {}".format(checksum(sys.argv[1])))
    print("Quotient total is {}".format(evenly_divisible(sys.argv[1])))
