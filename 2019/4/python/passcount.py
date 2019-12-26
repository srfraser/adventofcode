
from itertools import groupby


def main():
    low_range = 265275
    high_range = 781584

    count = 0
    # Part 1
    for current in range(low_range, high_range + 1):
        current = str(current)
        if sorted(current) != list(current):
            continue
        # if not any([current[i] == current[i+1] for i in range(len(current) -1)]):
        #    continue
    
        groups = [''.join(group) for _, group in groupby(current)]
        if len(groups) == len(current):
            continue
        count += 1 
    print("Counted passwords", count)

    # Part 2
    count = 0
    for current in range(low_range, high_range + 1):
        current = str(current)
        if sorted(current) != list(current):
            continue
        groups = [''.join(group) for _, group in groupby(current)]
        groups = [group for group in groups if len(group) == 2]
        if len(groups) == 0:
            continue
        count += 1 
    print("Counted passwords", count)


if __name__ == "__main__":
    main()
