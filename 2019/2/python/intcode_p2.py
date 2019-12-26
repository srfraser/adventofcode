


def run_program(intcode):
    current_opcode = 0

    while intcode[current_opcode] != 99:
        if intcode[current_opcode] == 1:
            intcode[intcode[current_opcode + 3]] = intcode[intcode[current_opcode + 1]] + intcode[intcode[current_opcode + 2]]
            current_opcode += 4
        elif intcode[current_opcode] == 2:
            intcode[intcode[current_opcode + 3]] = intcode[intcode[current_opcode + 1]] * intcode[intcode[current_opcode + 2]]
            current_opcode += 4
        else:
            print("Opcode error! Position", current_opcode)
            break
    
    return intcode


def main(filename):

    testcode = '1,9,10,3,2,3,11,0,99,30,40,50'
    test_program = [int(i) for i in testcode.split(',')]
    test_result = run_program(test_program)
    assert test_result == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    
    with open(filename) as f:
        program = [int(i) for i in f.read().rstrip().split(',')]

    saved_program = list(program)
    expected_output = 19690720

    # Fix initial input
    for noun in range(100):
        for verb in range(100):
            program = list(saved_program)
            program[1] = noun
            program[2] = verb
            new_program = run_program(program)
            if new_program[0] == expected_output:
                print("Found", noun, verb)
                break
            elif new_program[0] > expected_output:
                break   
    


if __name__ == '__main__':
    main('../input')
