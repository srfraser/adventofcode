def add(intcode, v1, v2, store, *args):
    intcode[store] = v1 + v2


def multiply(intcode, v1, v2, store, *args):
    intcode[store] = v1 * v2


def store(intcode, v1, store, *args):
    intcode[store] = v1


def retrieve(intcode, v1, *args):
    print(intcode[v1])


def jump_if_true(intcode, v1, v2, *args):
    if v1 != 0:
        return intcode[v2]


def jump_if_false(intcode, v1, v2, *args):
    if v1 == 0:
        return intcode[v2]


def less_than(intcode, v1, v2, store, *args):
    if v1 < v2:
        intcode[store] = 1
    else:
        intcode[store] = 0


def equals(intcode, v1, v2, store, *args):
    if v1 == v2:
        intcode[store] = 1
    else:
        intcode[store] = 0


OPERATIONS = {
    1: add,
    2: multiply,
    3: store,
    4: retrieve,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
}
OP_TAKES_INPUT = {3: True}
OP_STORE_PARAM = {1: 2, 2: 2, 3: 0, 4: 0, 5: 1, 6: 1, 7: 2, 8: 2}
ARG_COUNT = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}


def pad_modes(modes, arg_count):
    return f"{modes:0{arg_count}}"


def normalise_operation(opcode):
    opcode = str(opcode)
    operation = int(opcode[-2:])
    raw_modes = opcode[:-2] or 0

    modes = pad_modes(int(raw_modes), ARG_COUNT.get(operation, 0))
    modes = [int(i) for i in modes[::-1]]
    if OP_STORE_PARAM.get(operation) is not None:
        modes[OP_STORE_PARAM[operation]] = 1
    return operation, modes


def construct_operation(intcode, current_opcode):
    operation, modes = normalise_operation(intcode[current_opcode])
    if operation not in OPERATIONS:
        raise ValueError("Unknown operation: {} at position {}".format( operation, current_opcode))
    params = list()
    for offset, m in enumerate(modes, start=1):
        value = intcode[current_opcode + offset]
        if value == 1101:
            print(current_opcode, value, "operation", operation)
        if m == 0:
            value = intcode[value]
        params.append(value)
    return operation, params


def run_program(intcode, input_queue=None):
    current_opcode = 0

    if not input_queue:
        input_queue = list()

    code_length = len(intcode)
    while current_opcode < code_length and intcode[current_opcode] != 99:
        operation, params = construct_operation(intcode, current_opcode)
        if operation == 99:
            break
        if OP_TAKES_INPUT.get(operation, False):
            params = [input_queue.pop(0)] + params
        new_index = OPERATIONS[operation](intcode, *params)
        if new_index:
            current_opcode = new_index
        else:
            current_opcode += ARG_COUNT[operation] + 1

    return intcode


def main(filename):
    """
    assert normalise_operation(1) == (1, [0, 0, 1])
    assert normalise_operation(101) == (1, [1, 0, 1])
    assert normalise_operation(1001) == (1, [0, 1, 1])
    assert normalise_operation(10001) == (1, [0, 0, 1])
    assert normalise_operation(11101) == (1, [1, 1, 1])

    assert normalise_operation(2) == (2, [0, 0, 1])
    assert normalise_operation(102) == (2, [1, 0, 1])
    assert normalise_operation(1002) == (2, [0, 1, 1])
    assert normalise_operation(10002) == (2, [0, 0, 1])
    assert normalise_operation(11102) == (2, [1, 1, 1])

    assert normalise_operation(3) == (3, [1])
    assert normalise_operation(103) == (3, [1])

    testcode = "11002,4,3,4,33"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[1])
    assert test_result == [11002, 4, 3, 4, 99]

    testcode = "3,2,33"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[99])
    assert test_result == [3, 2, 99]

    with open("../../2/input") as f:
        program = [int(i) for i in f.read().rstrip().split(",")]
    program[2] = 2
    program[1] = 12
    test_result = run_program(program, input_queue=[99])
    assert test_result[0] == 3166704
    """
    with open(filename) as f:
        program = [int(i) for i in f.read().rstrip().split(",")]

    result = run_program(program, input_queue=[1])

    print("equal test, position mode, should be 0,1")
    testcode = "3,9,8,9,10,9,4,9,99,-1,8"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[0])
    test_result = run_program(test_program, input_queue=[8])

    print("equal test, immediate mode, should be 0,1")
    testcode = "3,3,1108,-1,8,3,4,3,99"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[0])
    test_result = run_program(test_program, input_queue=[8])

    print("less than test, position mode, should be 1,0")
    testcode = "3,9,7,9,10,9,4,9,99,-1,8"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[0])
    test_result = run_program(test_program, input_queue=[8])

    print("less than test, immediate mode, should be 1,0")
    testcode = "3,3,1107,-1,8,3,4,3,99"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[0])
    test_result = run_program(test_program, input_queue=[8])

    print("Jump tests, position mode, should be 0,1")
    testcode = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[0])

    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[1])

    print("Jump tests, immediate mode, should be 0,1")
    testcode = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[0])

    test_program = [int(i) for i in testcode.split(",")]
    test_result = run_program(test_program, input_queue=[1])


if __name__ == "__main__":
    main("../input")
