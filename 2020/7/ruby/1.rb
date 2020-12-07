require "set"

def process_rule_line(line)
  primary, containees = line.delete("\n").split(" contain ")
  primary.delete_suffix!(" bags")
  if containees.end_with?("no other bags.")
    return [primary, nil]
  end
  contents = containees.split(",").map(&:chomp).map { |details|
    details = details.chomp.delete_suffix(".").delete_suffix(" bags").delete_suffix(" bag")
    count, descr = details.split(" ", 2)
    [descr, count.to_i]
  }
  [primary, contents.to_h]
end

$cache = {}

def can_contain(rules, bag)
  if $cache.has_key?(bag)
    return $cache[bag]
  end
  found = rules.filter { |rule_name, rule|
    rule.is_a?(Hash) && rule.has_key?(bag)
  }.keys
  if !found.empty?
    found.each { |entry|
      found.concat(can_contain(rules, entry))
    }
    $cache[bag] = found.to_set.sort
  end

  found.to_set.sort
end

def process_part1_data(data)
  rules = data.lines.map { |line|
    process_rule_line(line)
  }.to_h
  can_contain(rules, "shiny gold").length
end

def count_containers(rules, bag, multiplier = 1)
  if $cache.has_key?(bag)
    return $cache[bag] * multiplier
  end
  if rules[bag].is_a?(Integer)
    $cache[bag] = rules[bag]
    return rules[bag] * multiplier
  end
  if rules[bag].nil?
    $cache[bag] = 0
    return $cache[bag]
  end
  rules[bag].map {
    |rule_name, rule|
    rule * multiplier + count_containers(rules, rule_name, rule * multiplier)
  }.inject(:+)
end

def process_part2_data(data)
  rules = data.lines.map { |line|
    process_rule_line(line)
  }.to_h
  count_containers(rules, "shiny gold")
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
puts "Part 1 test result: #{process_part1_data(test_data)}"

$cache = {}
input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
puts "Part 1 result: #{process_part1_data(real_data)}"

$cache = {}
input_file = File.join(File.dirname(__FILE__), "../test_input_part_2")
test_data = File.read(input_file)
puts "Part 2 test result: #{process_part2_data(test_data)}"

puts "Part 2 result: #{process_part2_data(real_data)}"
