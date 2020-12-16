class Constraint
  def initialize(string)
    string.chomp!
    @label, rest = string.split(": ")
    c1, _, c2 = rest.split

    @c1_min, @c1_max = c1.split("-").map(&:to_i)
    @c2_min, @c2_max = c2.split("-").map(&:to_i)
    # puts "#{string} => #{@c1_min},#{@c1_max} #{@c2_min},#{@c2_max}"
  end

  def is_valid?(number)
    # puts "Comparing #{number} to #{@c1_min},#{@c1_max} #{@c2_min},#{@c2_max}"
    if number >= @c1_min && number <= @c1_max
      return true
    elsif number >= @c2_min && number <= @c2_max
      return true
    else
      return false
    end
  end

  def label
    @label
  end
end

def process_file(filename)
  file_contents = File.read(filename)
  raw_constraints, raw_ticket, raw_others = file_contents.split("\n\n")

  constraints = raw_constraints.lines.map { |c| Constraint.new(c) }

  my_ticket = raw_ticket.delete("your ticket:\n").split(",").map(&:to_i)

  nearby_tickets = raw_others.delete("nearby_tickets: ")
    .lines.map(&:chomp)
    .select { |l| l != "" }
    .map { |l| l.split(",").map(&:to_i) }

  [constraints, my_ticket, nearby_tickets]
end

def invalid_tickets(filename)
  constraints, my_ticket, nearby_tickets = process_file(filename)

  nearby_tickets.map { |ticket|
    ticket.select { |n|
      constraints.select { |c| c.is_valid?(n) }.empty?
    }
  }.flatten.sum
end

def discard_invalid_tickets(nearby_tickets, constraints)
  nearby_tickets.select { |ticket|
    ticket.select { |n|
      constraints.select { |c| c.is_valid?(n) }.empty?
    }.empty?
  }
end

def determine_fields(tickets, constraints)
  ticket_columns = tickets.transpose

  # Can't filter as we go in case it's not the first one that only has
  # one matching constraint
  matching_constraints = ticket_columns.zip(0..).map { |col_data, index|
    [index, constraints.select { |c|
      col_data.select { |n|
        c.is_valid?(n)
      }.length == col_data.length
    }]
  }.to_h
  start = matching_constraints.select { |k, v| v.length == 1 }
  seen = Array.new
  matching_constraints.sort_by { |k, v| v.length }.map { |k, v|
    found = v.select { |c|
      !seen.include?(c)
    }
    seen += v
    [found[0].label, k]
  }.to_h
end

def part2_test(filename)
  constraints, my_ticket, nearby_tickets = process_file(filename)

  tickets = discard_invalid_tickets(nearby_tickets, constraints)
  determine_fields(tickets, constraints)
end

def part2(filename)
  constraints, my_ticket, nearby_tickets = process_file(filename)

  tickets = discard_invalid_tickets(nearby_tickets, constraints)
  field_map = determine_fields(tickets, constraints)

  field_map.select { |label, index| label.start_with?("departure") }.map { |label, index|
    my_ticket[index]
  }.inject(:*)
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
puts "Part 1 test result: #{invalid_tickets(input_file)}"

input_file = File.join(File.dirname(__FILE__), "../input")
puts "Part 1 result: #{invalid_tickets(input_file)}"

input_file = File.join(File.dirname(__FILE__), "../test_input_part_2")
puts "Part 2 test result: #{part2_test(input_file)}"

input_file = File.join(File.dirname(__FILE__), "../input")
puts "Part 2 result: #{part2(input_file)}"
