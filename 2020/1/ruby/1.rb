test_data = [
  1721,
  979,
  366,
  299,
  675,
  1456,
]

def search_part1(data, target)
  data.permutation(2).to_a.each { |a, b|
    return [a, b].inject(:*) if a + b == target
  }
end

def search_part2(data, num_factors, target)
  data.permutation(num_factors).to_a.each { |a|
    return a.inject(:*) if a.inject(:+) == target
  }
end

product = search_part1(test_data, 2020)
raise "Invalid test" unless product == 514579

input_file = File.join(File.dirname(__FILE__), "../input")
part1_data = File.readlines(input_file).map(&:to_i)

product = search_part1(part1_data, 2020)
puts "Part 1 result: #{product}"

product = search_part2(part1_data, 3, 2020)
puts "Part 2 result: #{product}"
