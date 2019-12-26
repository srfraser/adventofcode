


def turtle_to_coords(turtle):
    coords = [(0,0)]
    turtle = turtle.split(',')
    for operation in turtle:
        direction, magnitude = operation[0], int(operation[1:])
        current_x, current_y = coords[-1]
        if direction == 'R':
            for x in range(current_x + 1, current_x + magnitude + 1):
                coords.append((x, current_y))
        elif direction == 'L':
            for x in range(current_x - 1, current_x - magnitude - 1, -1):
                coords.append((x, current_y))
        if direction == 'U':
            for y in range(current_y + 1, current_y + magnitude + 1):
                coords.append((current_x, y))
        if direction == 'D':
            for y in range(current_y - 1, current_y - magnitude -1, -1):
                coords.append((current_x, y))
    return coords

def find_intersections(coords1, coords2):
    return set(coords1).intersection(set(coords2))

def manhattan(x, y):
    return abs(y) + abs(x)


def line_steps(cross, wire1, wire2):
    return wire1.index(cross) + wire2.index(cross) 

def main():
    with open('../input') as f:
        wire1_raw = f.readline()
        wire2_raw = f.readline()

    # wire1_raw = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    # wire2_raw = 'U62,R66,U55,R34,D71,R55,D58,R83'
    
    # wire1_raw = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    # wire2_raw = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

    wire1 = turtle_to_coords(wire1_raw)
    wire2 = turtle_to_coords(wire2_raw)

    crosspoints = find_intersections(wire1, wire2)
    crosspoints.remove((0,0))
    print(crosspoints)

    shortest = min([manhattan(x, y) for x,y in crosspoints])

    print(shortest)

    line_distances = dict()
    for cross in crosspoints:
        line_distances[cross] = line_steps(cross, wire1, wire2) 

    print(min(line_distances.values()))
    

if __name__ == '__main__':
    main()
