def unordered_maths(expression)
  while expression.match(/^(\d+ [\+\*] \d+)/)
    # puts "expression.sub('#{$1}', #{eval($1).to_s})"
    expression = expression.sub($1, eval($1).to_s)
  end
  expression
end

def addition_priority_maths(expression)
  while expression.match(/(\d+ \+ \d+)/)
    expression = expression.sub($1, eval($1).to_s)
  end
  while expression.match(/(\d+ \* \d+)/)
    expression = expression.sub($1, eval($1).to_s)
  end
  expression
end

def process_line(line, calculator)
  while line.match(/(\([^\(\)]+\))/)
    substr = $1.clone
    line = line.sub(substr, method(calculator).call(substr.delete("()")))
  end
  method(calculator).call(line).to_i
end

def do_homework(expressions, calculator)
  expressions.lines.map(&:chomp).map { |e| process_line(e, calculator) }.sum
end

test_cases = [
  ["2 * 3 + (4 * 5)", 26],
  ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 437],
  ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240],
  ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632],
]

for input, expected in test_cases
  puts "Part 1 test case #{process_line(input, :unordered_maths)} == #{expected}"
end

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
puts "Part 1 result: #{do_homework(real_data, :unordered_maths)}"
puts ""

test_cases_part_2 = [
  ["2 * 3 + (4 * 5)", 46],
  ["5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445],
  ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060],
  ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340],
]

for input, expected in test_cases_part_2
  puts "Part 2 test case #{process_line(input, :addition_priority_maths)} == #{expected}"
end
puts "Part 2 result: #{do_homework(real_data, :addition_priority_maths)}"
puts ""
