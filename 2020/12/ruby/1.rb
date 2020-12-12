FACING_MAP = { "N" => :north, "S" => :south, "E" => :east, "W" => :west }

def change_facing(current, instruction)
  facings = [:east, :south, :west, :north].cycle(2).to_a

  direction = instruction[0]
  magnitude = instruction[1..].to_i / 90

  if direction == "L"
    facings.reverse!
  end
  facings[facings.index(current) + magnitude]
end

def move_in_direction(location, direction, magnitude)
  if direction == :east
    location[0] += magnitude
  elsif direction == :south
    location[1] -= magnitude
  elsif direction == :west
    location[0] -= magnitude
  elsif direction == :north
    location[1] += magnitude
  end
  location
end

def take_evasive_action(course)
  ship_at = [0, 0]
  ship_facing = :east

  course.lines.map(&:chomp).each { |instr|
    if instr.start_with?("R") || instr.start_with?("L")
      ship_facing = change_facing(ship_facing, instr)
    elsif instr.start_with?("F")
      ship_at = move_in_direction(ship_at, ship_facing, instr[1..].to_i)
    else
      ship_at = move_in_direction(ship_at, FACING_MAP[instr[0]], instr[1..].to_i)
    end
    # puts "Ship follows #{instr}, now at #{ship_at} facing #{ship_facing}"
  }

  ship_at[0].abs + ship_at[1].abs
end

def rotate_waypoint(location, instruction)
  direction = instruction[0]
  magnitude = instruction[1..].to_i / 90

  if direction == "R"
    (1..magnitude).each {
      location[0], location[1] = location[1], -location[0]
    }
  else
    (1..magnitude).each {
      location[0], location[1] = -location[1], location[0]
    }
  end
  location
end

def take_evasive_waypoint_action(course)
  ship_at = [0, 0]
  waypoint_at = [10, 1]
  ship_facing = :east

  course.lines.map(&:chomp).each { |instr|
    if instr.start_with?("R") || instr.start_with?("L")
      waypoint_at = rotate_waypoint(waypoint_at, instr)
    elsif instr.start_with?("F")
      (1..instr[1..].to_i).to_a.each {
        ship_at[0] += waypoint_at[0]
        ship_at[1] += waypoint_at[1]
      }
    else
      waypoint_at = move_in_direction(waypoint_at, FACING_MAP[instr[0]], instr[1..].to_i)
    end
    # puts "Ship follows #{instr}, now at #{ship_at} facing #{ship_facing}"
  }

  ship_at[0].abs + ship_at[1].abs
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
puts "Part 1 test result: #{take_evasive_action(test_data)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
puts "Part 1 result: #{take_evasive_action(real_data)}"

puts "Part 2 test result: #{take_evasive_waypoint_action(test_data)}"
puts "Part 2 result: #{take_evasive_waypoint_action(real_data)}"
