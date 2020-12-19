def process_single_rule(rule_id, rules_map)
  rule = rules_map[rule_id]
  potentials = rule.split("|").map(&:split)
  puts "potentials #{potentials}"
  expanded = potentials.map { |p|
    p1 = p.map { |r|
      puts "Examining #{r}"
      if r.length == 3 && r.start_with?('"') && r.end_with?('"')
        puts "resolving to #{r.split("")[1]}"
        r.split("")[1]
      elsif r == rule_id
        "\\g<0>?"
      else
        puts "Calling process_single_rule(#{r}, map)"
        process_single_rule(r, rules_map)
      end
    }.flatten
    p1 = p1.join("")
    puts "Decided on #{p1}"
    p1
  }
  expanded = expanded.join("|")
  puts "Now have #{expanded}"
  if expanded.length > 1
    puts "long expanded"
    expanded = "(#{expanded})"
  end
  expanded
end

def expand_rules(raw_rules_content)
  rules_map = raw_rules_content.lines.map(&:chomp).map { |r|
    r.split(": ")
  }.to_h

  process_single_rule("0", rules_map)
end

def process_input_file(input_file)
  contents = File.read(input_file)
  rules, messages = contents.split("\n\n")
  [expand_rules(rules), messages.lines.map(&:chomp)]
end

def part1(rule, messages)
  messages.select { |m| m.match(/^#{rule}$/) }.length
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_rules, test_messages = process_input_file(input_file)
puts "#{test_rules}"
puts "Part 1 test result: #{part1(test_rules, test_messages)} == 2"

input_file = File.join(File.dirname(__FILE__), "../input")
rule, messages = process_input_file(input_file)
puts "Part 1 result: #{part1(rule, messages)}"

input_file = File.join(File.dirname(__FILE__), "../test_input_part_2")
test_rules, test_messages = process_input_file(input_file)
puts "#{test_rules}"
puts "Part 1 test before modifying rules: #{part1(test_rules, test_messages)} == 3"

input_file = File.join(File.dirname(__FILE__), "../test_input_part_2_rules_replaced")
test_rules, test_messages = process_input_file(input_file)
puts "#{test_rules}"
puts "Part 1 test after modifying rules: #{part1(test_rules, test_messages)} == 12"

#input_file = File.join(File.dirname(__FILE__), "../input_rules_replaced")
#rule, messages = process_input_file(input_file)
#puts "Part 2 result: #{part1(rule, messages)}"
