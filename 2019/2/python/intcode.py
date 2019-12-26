


def run_program(intcode):
    current_opcode = 0

    while intcode[current_opcode] != 99:
        if intcode[current_opcode] == 1:
            intcode[intcode[current_opcode + 3]] = intcode[intcode[current_opcode + 1]] + intcode[intcode[current_opcode + 2]]
        elif intcode[current_opcode] == 2:
            intcode[intcode[current_opcode + 3]] = intcode[intcode[current_opcode + 1]] * intcode[intcode[current_opcode + 2]]
        else:
            print("Opcode error! Position", current_opcode)
            break
        current_opcode += 4
    
    return intcode


def main(filename):

    testcode = '1,9,10,3,2,3,11,0,99,30,40,50'
    test_program = [int(i) for i in testcode.split(',')]
    test_result = run_program(test_program)
    assert test_result == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    
    with open(filename) as f:
        program = [int(i) for i in f.read().rstrip().split(',')]

    # Fix initial input
    program[1] = 12
    program[2] = 2

    new_program = run_program(program)
    print(new_program[0])
    


if __name__ == '__main__':
    main('../input')
