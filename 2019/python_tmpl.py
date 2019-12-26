
import sys

def part1(input_file):
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    part1(filename)