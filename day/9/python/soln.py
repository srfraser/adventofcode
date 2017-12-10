import sys
import re


def strip_cancellations(data):
    return re.sub(r'!.', '', data)


def strip_garbage(data):
    data = strip_cancellations(data)
    return re.sub(r'\<.*?\>', '', data)


def score(data):
    total_score = 0
    current_score = 0

    for char in data:
        if char == '{':
            current_score += 1
        elif char == '}':
            total_score += current_score
            current_score -= 1
    return total_score


def part1(data):
    data = strip_garbage(data)
    data = data.replace(',', '')
    print("Score is {}".format(score(data)))


def part2(data):
    data = strip_cancellations(data)
    nocancel_length = len(data)
    num_garbage_indicators = len(re.findall(r'(\<.*?\>)', data)) * 2
    data = strip_garbage(data)
    garbage_len = nocancel_length - num_garbage_indicators - len(data)
    print("Number of garbage characters: {}".format(garbage_len))


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readline()
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
