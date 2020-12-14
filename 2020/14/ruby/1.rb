def parse_mem_instruction(str)
  matches = str.match(/mem\[(\d+)\] = (\d+)/)
  [matches[1].to_i, matches[2].to_i]
end

def run_part1(data)
  memory = Hash.new
  mask = []
  data.lines.each { |line|
    if line.start_with?("mask")
      mask = line.split(" = ")[1]
    else
      address, value = parse_mem_instruction(line)
      value = value.to_s(2).rjust(36, "0").split("")
      value.each_with_index { |v, i|
        if mask[i] != "X"
          value[i] = mask[i]
        end
      }
      memory[address] = value.join.to_i(2)
    end
  }
  memory.values.inject(:+)
end

# Rosetta code func_power_set
class Array
  # A more functional and even clearer variant.
  def func_power_set
    inject([[]]) { |ps, item| # for each item in the Array
      ps + # take the powerset up to now and add
      ps.map { |e| e + [item] } # it again, with the item appended to each element
    }
  end
end

def run_part2(data)
  memory = Hash.new
  mask = ""

  data.lines.each { |line|
    if line.start_with?("mask")
      mask = line.split(" = ")[1].chomp.split("")
    else
      address, value = parse_mem_instruction(line)
      base = address.clone
      address = address.to_s(2).rjust(36, "0").split("")

      address = address.zip(mask).map { |b, m|
        if m == "X" || m == "1"
          m
        else
          b
        end
      }
      xs = address.zip(0..).select { |a, index| a == "X" }.map { |a, index| index }
      xs.func_power_set.each { |bits|
        xs.each { |settable|
          if bits.include?(settable)
            address[settable] = 1
          else
            address[settable] = 0
          end
        }
        memory[address.join.to_i(2)] = value
      }
    end
  }
  memory.values.sum
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
puts "Part 1 test result: #{run_part1(test_data)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
puts "Part 1 result: #{run_part1(real_data)}"

input_file = File.join(File.dirname(__FILE__), "../test_input_part_2")
test_data = File.read(input_file)
puts "Part 1 test result: #{run_part2(test_data)}"

puts "Part 1 result: #{run_part2(real_data)}"
