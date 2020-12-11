require "ruby-enum"

class Seat
  include Ruby::Enum

  define :EMPTY_SEAT, "L"
  define :TAKEN_SEAT, "#"
  define :FLOOR, "."
end

def process_seat_map(data)
  data.lines.each_with_index.map { |line, line_number|
    line.chomp.split("").each_with_index.map { |char, char_index|
      [[char_index, line_number], Seat.key(char)]
    }
  }.flatten(1).to_h
end

$adjacencies = {}

def adjacent_to(seat, max_x, max_y)
  if !$adjacencies.has_key?(seat)
    x = seat[0]
    y = seat[1]
    $adjacencies[seat] = ([0, y - 1].max..[max_y, y + 1].min).map { |y1|
      ([0, x - 1].max..[max_x, x + 1].min).map { |x1|
        [x1, y1]
      }
    }.flatten(1).select { |new_seat| new_seat != seat }
  end
  return $adjacencies[seat]
end

def visible_to(seat_map, seat, max_x, max_y)
  directions = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1],
  ]

  located = Array.new
  for direction in directions
    found = false
    multiplier = 1
    while !found
      x = seat[0] + multiplier * direction[0]
      y = seat[1] + multiplier * direction[1]
      # puts "Examining #{x},#{y} which is #{seat_map[[x, y]]}"
      if x < 0 || x > max_x || y < 0 || y > max_y
        found = true
      else
        if seat_map[[x, y]] == :FLOOR
          multiplier += 1
        else
          found = true
          located.append([x, y])
        end
      end
    end
  end
  # puts "#{seat} can see #{located}"
  located
end

def count_occupied_adjacent_seat(seat_map, seat, max_x, max_y)
  adjacent_to(seat, max_x, max_y).select { |s| seat_map[s] == :TAKEN_SEAT }.length
end

def count_occupied_visible_seat(seat_map, seat, max_x, max_y)
  visible_to(seat_map, seat, max_x, max_y).select { |s| seat_map[s] == :TAKEN_SEAT }.length
end

def seat_iteration(seat_map, max_x, max_y, tolerance)
  seat_map.map { |seat, occ|
    adj = count_occupied_adjacent_seat(seat_map, seat, max_x, max_y)
    if occ == :EMPTY_SEAT && adj == 0
      changes = true
      [seat, :TAKEN_SEAT]
    elsif occ == :TAKEN_SEAT && adj >= tolerance
      changes = true
      [seat, :EMPTY_SEAT]
    else
      [seat, occ]
    end
  }.to_h
end

def seat_iteration_part2(seat_map, max_x, max_y, tolerance)
  seat_map.map { |seat, occ|
    adj = count_occupied_visible_seat(seat_map, seat, max_x, max_y)

    if occ == :EMPTY_SEAT && adj == 0
      changes = true
      [seat, :TAKEN_SEAT]
    elsif occ == :TAKEN_SEAT && adj >= tolerance
      changes = true
      [seat, :EMPTY_SEAT]
    else
      [seat, occ]
    end
  }.to_h
end

def display_seat_map(seat_map, max_x, max_y)
  (0..max_y).each { |y|
    (0..max_x).each { |x|
      print(Seat.value(seat_map[[x, y]]))
    }
    print("\n")
  }
end

def process_part1_data(seat_map, tolerance)
  max_x = seat_map.keys.map { |v| v[0] }.max
  max_y = seat_map.keys.map { |v| v[1] }.max

  iteration = 0
  differences = 1
  while differences > 0
    t1 = Time.now
    new_seat_map = seat_iteration(seat_map, max_x, max_y, tolerance)
    t2 = Time.now
    differences = new_seat_map.select { |seat, occ| seat_map[seat] != occ }.length
    # puts "iteration #{iteration}, differences #{differences}, #{t2 - t1}"
    iteration += 1
    # display_seat_map(new_seat_map, max_x, max_y)
    seat_map = new_seat_map.clone
  end

  new_seat_map.select { |seat, occ| occ == :TAKEN_SEAT }.length
end

def process_part2_data(seat_map, tolerance)
  max_x = seat_map.keys.map { |v| v[0] }.max
  max_y = seat_map.keys.map { |v| v[1] }.max

  iteration = 0
  differences = 1
  while differences > 0
    t1 = Time.now
    new_seat_map = seat_iteration_part2(seat_map, max_x, max_y, tolerance)
    t2 = Time.now
    differences = new_seat_map.select { |seat, occ| seat_map[seat] != occ }.length
    # puts "iteration #{iteration}, differences #{differences}, #{t2 - t1}"
    iteration += 1
    # display_seat_map(new_seat_map, max_x, max_y)
    seat_map = new_seat_map.clone
  end

  # display_seat_map(seat_map, max_x, max_y)
  new_seat_map.select { |seat, occ| occ == :TAKEN_SEAT }.length
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
test_seat_map = process_seat_map(test_data)
puts "Part 1 test result: #{process_part1_data(test_seat_map, 4)}"
$adjacencies = {}

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
real_seat_map = process_seat_map(real_data)
puts "Part 1 result: #{process_part1_data(real_seat_map, 4)}"

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
test_seat_map = process_seat_map(test_data)
puts "Part 2 test result: #{process_part2_data(test_seat_map, 5)} == 26 "

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
real_seat_map = process_seat_map(real_data)
puts "Part 1 result: #{process_part2_data(real_seat_map, 5)}"
