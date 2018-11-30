

gen_a_seed = 116
gen_b_seed = 299

gen_a_factor = 16807
gen_b_factor = 48271


def mygenerator(seed, factor, remainder=None):
    current = seed
    while True:
        current = (current * factor) % 2147483647
        if not remainder:
            yield current
        elif remainder and current % remainder == 0:
            yield current


def main():
    total = 0
    counter = 0
    for a, b in zip(mygenerator(gen_a_seed, gen_a_factor), mygenerator(gen_b_seed, gen_b_factor)):
        counter += 1
        if counter >= 40000000:
            break
        # if bin(a & 0xFFFF) == bin(b & 0xFFFF):
        if a & 0xFFFF == b & 0xFFFF:
            total += 1
    print("Part 1 found {} matches".format(total))

    total = 0
    counter = 0
    for a, b in zip(mygenerator(gen_a_seed, gen_a_factor, remainder=4), mygenerator(gen_b_seed, gen_b_factor, remainder=8)):
        counter += 1
        if counter >= 5000000:
            break
        # if bin(a & 0xFFFF) == bin(b & 0xFFFF):
        if a & 0xFFFF == b & 0xFFFF:
            total += 1
    print("Part 2 found {} matches".format(total))


if __name__ == '__main__':
    main()
