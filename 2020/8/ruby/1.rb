def process_intructions(data)
  data.lines.map { |entry|
    [*entry.split]
  }
end

def find_accumulator_value(instructions)
  positions_seen = []
  current_position = 0
  accumulator = 0

  until positions_seen.include?(current_position)
    if current_position > instructions.length
      return accumulator
    end

    instruction, value = instructions[current_position]
    positions_seen.append(current_position)
    if instruction == "acc"
      accumulator += value.to_i
      current_position += 1
    elsif instruction == "jmp"
      current_position += value.to_i
    else
      current_position += 1
    end
  end
  accumulator
end

def does_it_end(instructions)
  positions_seen = []
  current_position = 0
  accumulator = 0

  until positions_seen.include?(current_position)
    if current_position > instructions.length
      return true
    end
    instruction, value = instructions[current_position]
    positions_seen.append(current_position)
    if instruction == "acc"
      accumulator += value.to_i
      current_position += 1
    elsif instruction == "jmp"
      current_position += value.to_i
    else
      current_position += 1
    end
  end
  false
end

# We are allowed to swap nop<->jmp
# We want to reach the end of the instructions,
# so good candidates are:
# jmp negative -> nop
# nop positive -> jmp
# start near the end
def check_candidates_for_replacement(instructions)
  instructions.lazy.each_with_index { |cmd, index|
    instr, val = cmd
    val = val.to_i
    if instr == "jmp" && val < 0
      new_instructions = instructions.clone
      new_instructions[index] = ["nop", val]

      if does_it_end(new_instructions)
        return new_instructions
      end
    elsif instr == "nop" && val > 0
      new_instructions = instructions.clone
      new_instructions[index] = ["jmp", val]

      if does_it_end(new_instructions)
        return new_instructions
      end
    end
  }
end

def process_part1_data(data)
  instructions = process_intructions(data)
  find_accumulator_value(instructions)
end

def process_part2_data(data)
  instructions = process_intructions(data)
  this_ends = check_candidates_for_replacement(instructions)
  find_accumulator_value(this_ends)
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
puts "Part 1 test result: #{process_part1_data(test_data)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
puts "Part 1 result: #{process_part1_data(real_data)}"

puts "Part 2 test result: #{process_part2_data(test_data)}"
puts "Part 2 result: #{process_part2_data(real_data)}"
