import math


def fuel_required(mass):
    return max(0, math.floor(float(mass)/3) - 2)


def fuel_required_fuel(mass):
    basic = fuel_required(mass)
    additional_required = basic
    while additional_required > 0:
        additional_required = fuel_required(additional_required)
        basic += additional_required
    return basic


def main():
    assert fuel_required(12) == 2
    assert fuel_required(14) == 2
    assert fuel_required(1969) == 654
    assert fuel_required(100756) == 33583

    with open('../input') as f:
        module_weights = [float(l) for l in f.readlines()]
    first_round_fuel = sum([fuel_required(w) for w in module_weights])
    print("Part 1", first_round_fuel)

    assert fuel_required_fuel(14) == 2
    assert fuel_required_fuel(1969) == 966
    assert fuel_required_fuel(100756) == 50346

    second_round_fuel = sum([fuel_required_fuel(w) for w in module_weights])
    print("Part 2", second_round_fuel)


if __name__ == '__main__':
    main()
