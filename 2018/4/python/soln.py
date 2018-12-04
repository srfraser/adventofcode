
import sys
from datetime import datetime, timedelta
from collections import defaultdict

from dateutil.rrule import rrule, MINUTELY

def part1(input_file):
    with open(input_file) as f:
        data = f.readlines()

    dataset = dict()
    for line in data:
        timestamp = datetime.strptime(line.split(']')[0], '[%Y-%m-%d %H:%M')
        dataset[timestamp] = line.split(']')[1]

    current_guard = None
    start = None
    end = None
    guard_record = defaultdict(list)
    for timestamp in sorted(dataset):
        text = dataset[timestamp]
        if 'begins shift' in text:
            current_guard = text.split()[1]
        elif 'falls asleep' in text:
            start = timestamp
        elif 'wakes up' in text:
            end = timestamp
            guard_record[current_guard].append((start, end))

    # total amount slept
    sleep_durations = dict()
    for guard in guard_record:
        sleep_durations[guard] = timedelta(0)
        for sleeps in guard_record[guard]:
            sleep_durations[guard] += sleeps[1] - sleeps[0]

    laziest = max(sleep_durations, key=sleep_durations.get)
    print("Part 1: Laziest guard:", laziest)

    # Most common minute spent asleep
    minutes = defaultdict(int)
    for sleeps in guard_record[laziest]:
        for minute in rrule(MINUTELY, interval=1, dtstart=sleeps[0], until=sleeps[1]):
            minutes[minute.minute] += 1

    most_common_minute = max(minutes, key=minutes.get)
    print("Part 1: Most common minute: ", most_common_minute)

    print("Part 1: Checksum: ", int(laziest.replace('#','')) * most_common_minute)

    most_common = dict()
    for guard in guard_record:
        minutes = defaultdict(int)
        for sleeps in guard_record[guard]:
            for minute in rrule(MINUTELY, interval=1, dtstart=sleeps[0], until=sleeps[1]):
                minutes[minute.minute] += 1
        mc = max(minutes, key=minutes.get)
        most_common[guard] = (mc, minutes[mc])

    part2_combo = max(most_common, key=lambda x: most_common.get(x)[1])
    print("Part 2: Most common minute/guard combo: ", part2_combo, most_common[part2_combo])
    print("Part 2: Checksum: ", int(part2_combo.replace('#', '')) * most_common[part2_combo][0])



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    part1(filename)