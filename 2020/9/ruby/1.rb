def find_first_invalid(data, preamble)
  candidates = data.take(preamble)
  data = data[preamble..]

  data.each { |d|
    sums = candidates.combination(2).to_a.map { |a| a.inject(:+) }
    if !sums.include?(d)
      return d
    end
    candidates.shift()
    candidates.append(d)
  }
end

def find_contiguous_components(data, target)
  (0..data.index(target) - 1).each { |lower|
    (1..data.index(target)).each { |upper|
      if data[lower..upper].inject(:+) == target
        return data[lower..upper]
      end
    }
  }
end

def process_part1_data(data, preamble)
  find_first_invalid(data, preamble)
end

def process_part2_data(data, preamble)
  components = find_contiguous_components(data, find_first_invalid(data, preamble))
  [components.min, components.max].inject(:+)
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file).lines.map(&:to_i)
puts "Part 1 test result: #{process_part1_data(test_data, 5)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file).lines.map(&:to_i)
puts "Part 1 result: #{process_part1_data(real_data, 25)}"

puts "Part 2 test result: #{process_part2_data(test_data, 5)}"
puts "Part 2 result: #{process_part2_data(real_data, 25)}"
