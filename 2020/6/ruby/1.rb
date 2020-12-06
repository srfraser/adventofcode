require "set"

def process_part1_data(raw_data)
  raw_data.split("\n\n").map { |entry|
    entry.delete("\n").delete(" ").split("").to_set.length
  }.inject(:+)
end

def process_part2_data(raw_data)
  raw_data.split("\n\n").map { |entry|
    people = entry.split("\n").length
    values = entry.delete("\n").split("").to_set.select { |v|
      entry.count(v) == people
    }
    values.length
  }.inject(:+)
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
puts "Part 1 test result: #{process_part1_data(test_data)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
puts "Part 1 result: #{process_part1_data(real_data)}"

puts "Part 2 test result: #{process_part2_data(test_data)}"
puts "Part 2 result: #{process_part2_data(real_data)}"
