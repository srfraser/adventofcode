def part1(data)
  valid = 0
  data.each { |d|
    min, max, letter, password = d.split(/[- :]+/)
    count = password.count(letter)
    if min.to_i <= count && count <= max.to_i
      valid += 1
    end
  }
  valid
end

def part2(data)
  valid = 0
  data.each { |d|
    pos1, pos2, letter, password = d.split(/[- :]+/)
    value1 = password[pos1.to_i - 1]
    value2 = password[pos2.to_i - 1]
    next if value1 == value2

    if value1 == letter || value2 == letter
      valid += 1
    end
  }
  valid
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.readlines(input_file)

puts "Test valid entries: #{part1(test_data)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.readlines(input_file)

puts "Part 1 valid entries: #{part1(real_data)}"

puts "Test part 2 valid entries: #{part2(test_data)}"
puts "Part 2 valid entries: #{part2(real_data)}"
