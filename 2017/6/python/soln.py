import sys


def most_blocks(bank):
    return bank.index(max(bank))


def init_bank(filename):
    with open(filename, 'r') as f:
        data = f.readline()
    return [int(i) for i in data.split()]


def redistribute(bank):
    index = most_blocks(bank)
    to_spend = bank[index]
    bank[index] = 0

    while to_spend:
        index += 1
        index %= len(bank)
        to_spend -= 1
        bank[index] += 1
    return bank


def main():
    bank = init_bank(sys.argv[1])
    print(bank)

    seen = list()

    count = 0
    while bank not in seen:
        seen.append(list(bank))
        bank = redistribute(bank)
        count += 1

    print("Cycles until duplicate: {} or possibly {}".format(count, len(seen)))
    print("Cycles between that duplicate and the first: {}".format(len(seen) - seen.index(bank)))


if __name__ == '__main__':
    main()
