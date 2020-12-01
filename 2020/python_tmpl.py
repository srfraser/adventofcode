
import sys
from pathlib import Path

def part1(input_file):
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = Path(sys.argv[1])
    else:
        import os
        filename = Path(os.path.dirname(__file__)) / "../input"
    part1(filename)