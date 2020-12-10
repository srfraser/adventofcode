require "set"

def counter(data)
  data.to_set.map { |key|
    [key, data.count(key)]
  }.to_h
end

def process_part1_data(data)
  data.sort!
  data.unshift(0)

  differences = data.zip(data[1..]).map { |pair|
    # Can't append the final element without comparing it to nil
    # instead
    if pair[1].nil?
      3
    else
      pair[1] - pair[0]
    end
  }

  diff_count = counter(differences)
  puts "differences #{diff_count}"
  diff_count[1] * diff_count[3]
end

$cache = {}

def possibility(data)
  candidates = data[1..3].select { |d| d - data[0] <= 3 }
  if candidates.empty?
    return 1
  end
  candidates.map { |candidate|
    if !$cache.has_key?(candidate)
      $cache[candidate] = possibility(data[data.index(candidate)..])
    end
    $cache[candidate]
  }.inject(:+)
end

def process_part2_data(data)
  data.sort!
  data.unshift(0)
  puts "#{data}"
  possibility(data)
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file).lines.map(&:to_i)
puts "Part 1 test result: #{process_part1_data(test_data)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file).lines.map(&:to_i)
puts "Part 1 result: #{process_part1_data(real_data)}"

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file).lines.map(&:to_i)
puts "Part 2 test result: #{process_part2_data(test_data)}, expected 19208"

$cache = {}

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file).lines.map(&:to_i)
puts "Part 2 result: #{process_part2_data(real_data)}"
