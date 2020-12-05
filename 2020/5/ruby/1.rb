def bsearch(range, instructions, upper_indicator = "B", lower_indicator = "F")
  possibilities = (0..range).to_a
  instructions = instructions.split("")
  while half = instructions.shift
    if half == lower_indicator
      possibilities = possibilities[0..possibilities.length / 2]
    else
      possibilities = possibilities[possibilities.length / 2..]
    end
  end
  possibilities[0]
end

def find_row(instructions)
  bsearch(127, instructions[0..6])
end

def find_column(instructions)
  bsearch(7, instructions[7..], upper_indicator = "R", lower_indicator = "L")
end

def find_seat_id(instructions)
  (find_row(instructions) * 8) + find_column(instructions)
end

raise "Wrong bsearch" if bsearch(127, "FBFBBFF") != 44
raise "Wrong bsearch" if bsearch(127, "BFFFBBF") != 70
raise "Wrong bsearch" if bsearch(127, "FFFBBBF") != 14
raise "Wrong bsearch" if bsearch(127, "BBFFBBF") != 102

raise "Wrong row" if find_row("FBFBBFFRLR") != 44
raise "Wrong row" if find_row("BFFFBBFRRR") != 70
raise "Wrong row" if find_row("FFFBBBFRRR") != 14
raise "Wrong row" if find_row("BBFFBBFRLL") != 102

raise "Wrong column" if find_column("FBFBBFFRLR") != 5
raise "Wrong column" if find_column("BFFFBBFRRR") != 7
raise "Wrong column" if find_column("FFFBBBFRRR") != 7
raise "Wrong column" if find_column("BBFFBBFRLL") != 4

raise "Wrong seat_id" if find_seat_id("FBFBBFFRLR") != 357
raise "Wrong seat_id" if find_seat_id("BFFFBBFRRR") != 567
raise "Wrong seat_id" if find_seat_id("FFFBBBFRRR") != 119
raise "Wrong seat_id" if find_seat_id("BBFFBBFRLL") != 820

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)

real_data = real_data.split("\n")
seat_ids = real_data.map { |seat| find_seat_id(seat) }

puts "Part 1 highest seat id: #{seat_ids.max}"

min_seat_id = seat_ids.min
missing_seat = (seat_ids.min..seat_ids.max).sum - seat_ids.sum
puts "Part 2, missing seat ID: #{missing_seat}"
