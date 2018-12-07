
import sys
from collections import defaultdict
import string


def build_dependency_graph(raw_data):
    g = defaultdict(list)

    for line in raw_data:
        fields = line.split()
        g[fields[7]].append(fields[1])
        if fields[1] not in g:
            g[fields[1]] = list()
    return g


def find_runnable_tasks(graph, scheduled):
    runnable = list()
    for task in graph:
        if all([d in scheduled for d in graph[task]]):
            runnable.append(task)
    return runnable


def part1(graph):
    print(graph)

    schedule = list()

    while graph:
        runnable = sorted(find_runnable_tasks(graph, schedule))
        print(runnable)
        schedule.append(runnable[0])
        del graph[runnable[0]]

    print("".join(schedule))


def task_duration(task_id):
    return string.ascii_uppercase.index(task_id) + 1 + 60


def tick(workers):
    for worker in workers:
        if workers[worker] != None:
            workers[worker] = (workers[worker][0], workers[worker][1] - 1)
    return workers


def part2(graph, workers_count=5):
    print("Part 2: ", graph)

    workers = {i: None for i in range(workers_count)}
    print(workers)

    scheduled = list()
    completed = list()

    timer = 0

    target_completed = len(graph)

    while len(completed) < target_completed:
        for worker in workers:
            if workers[worker] and workers[worker][1] <= 0:
                print("Finished worker ", workers[worker])
                completed.append(workers[worker][0])
                workers[worker] = None

        if all([i != None for i in workers.values()]):
            timer += 1
            workers = tick(workers)
            continue

        runnable = sorted(find_runnable_tasks(graph, completed))

        for available in runnable:
            for worker in workers:
                if workers[worker] == None:
                    workers[worker] = (available, task_duration(available))
                    scheduled.append(available)
                    del graph[available]
                    break
        timer += 1
        workers = tick(workers)
        print(workers, timer)

    print("".join(scheduled))
    print(timer-1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        import os
        filename = os.path.join(os.path.dirname(__file__), '..', 'input')
    with open(filename) as f:
        data = f.readlines()

    graph = build_dependency_graph(data)
    part1(graph)
    graph = build_dependency_graph(data)
    part2(graph)
