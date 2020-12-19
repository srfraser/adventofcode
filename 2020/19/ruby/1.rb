def process_rules(rule_id, rules_map, depth)
  if depth > 20
    return ""
  end
  rstr = "("
  rule = rules_map[rule_id]
  rule.split.each { |r|
    if r == "|"
      rstr += r
    elsif (Integer(r) rescue false)
      rstr += process_rules(r, rules_map, depth + 1)
    else
      return r[1]
    end
  }
  rstr + ")"
end

def expand_rules(raw_rules_content)
  rules_map = raw_rules_content.lines.map(&:chomp).map { |r|
    r.split(": ")
  }.to_h

  process_rules("0", rules_map, 0)
end

def process_input_file(input_file)
  contents = File.read(input_file)
  rules, messages = contents.split("\n\n")
  [expand_rules(rules), messages.lines.map(&:chomp)]
end

def solve(rules, messages)
  messages.select { |m|
    m.match(/^#{rules}$/)
  }.length
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_rules, test_messages = process_input_file(input_file)
puts "Part 1 test result: #{solve(test_rules, test_messages)} == 2"

input_file = File.join(File.dirname(__FILE__), "../input")
rule, messages = process_input_file(input_file)
puts "Part 1 result: #{solve(rule, messages)}"

input_file = File.join(File.dirname(__FILE__), "../test_input_part_2")
test_rules, test_messages = process_input_file(input_file)
#puts "#{test_rules}"
puts "Part 2 test before modifying rules: #{solve(test_rules, test_messages)} == 3"

input_file = File.join(File.dirname(__FILE__), "../test_input_part_2_rules_replaced")
test_rules, test_messages = process_input_file(input_file)
#puts "#{test_rules}"
puts "Part 2 test after modifying rules: #{solve(test_rules, test_messages)} == 12"

input_file = File.join(File.dirname(__FILE__), "../input_rules_replaced")
rule, messages = process_input_file(input_file)
puts "Part 2 result: #{solve(rule, messages)}"
