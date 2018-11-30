
import sys


def count_valid(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == len(set(words)):
                count += 1
    return count


def count_valid_anagrams(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            words = [str(sorted(w)) for w in line.split()]
            if len(words) == len(set(words)):
                count += 1
    return count


if __name__ == '__main__':
    print(count_valid(sys.argv[1]))
    print(count_valid_anagrams(sys.argv[1]))
