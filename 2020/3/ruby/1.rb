def trees(map, across, down)
  tree_count = 0
  x, y = 0, 0
  while y < map.length
    row = map[y].clone
    if map[y][x] == "#"
      tree_count += 1
    end
    x = (x + across) % map[0].length
    y += down
  end
  tree_count
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
test_data = test_data.split("\n")
puts "Test trees hit: #{trees(test_data, across = 3, down = 1)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
real_data = real_data.split("\n")
puts "Part 1 trees hit: #{trees(real_data, across = 3, down = 1)}"

routes = [
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2],
]

product = routes.map { |across, down|
  trees(test_data, across, down)
}
puts "Part 2 test result: #{product}"
product = routes.map { |across, down|
  trees(test_data, across, down)
}.inject(:*)
puts "Part 2 test result: #{product}"

product = routes.map { |across, down|
  trees(real_data, across, down)
}

puts "Part 2 result: #{product}"
product = routes.map { |across, down|
  trees(real_data, across, down)
}.inject(:*)

puts "Part 2 result: #{product}"
