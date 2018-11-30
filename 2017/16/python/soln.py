
import sys
import string


class Troupe(object):
    def __init__(self):
        self._troupe = list(string.ascii_lowercase[:16])

    @property
    def troupe(self):
        return "".join(self._troupe)

    def execute(self, move):
        if move[0] == 's':
            self.spin(int(move[1:]))
        elif move[0] == 'x':
            m1, m2 = [int(i) for i in move[1:].split('/')]
            self.exchange(m1, m2)
        elif move[0] == 'p':
            m1, m2 = move[1:].split('/')
            self.exchange(self._troupe.index(m1), self._troupe.index(m2))

    def spin(self, count):
        self._troupe[:] = self._troupe[-count:] + self._troupe[:len(self._troupe) - count]

    def exchange(self, index1, index2):
        self._troupe[index1], self._troupe[index2] = self._troupe[index2], self._troupe[index1]


def main():
    with open(sys.argv[1], 'r') as f:
        dance_moves = f.readline().split(',')

    troupe = Troupe()

    starting_position = troupe.troupe

    iterations = 1000000000

    # Find the repetition
    for i in range(1, iterations):
        dm = list(dance_moves)
        while dm:
            troupe.execute(dm.pop(0))
        position = troupe.troupe
        if position == starting_position:
            print("Found starting position again at iteration {}".format(i))
            break

    actual_iterations = iterations % i

    print("Doing {} % {} = {} actual iterations from start".format(iterations, i, actual_iterations))

    troupe = Troupe()
    for i in range(actual_iterations):
        dm = list(dance_moves)
        while dm:
            troupe.execute(dm.pop(0))
        position = troupe.troupe

    print("".join(troupe.troupe))


if __name__ == '__main__':
    main()
