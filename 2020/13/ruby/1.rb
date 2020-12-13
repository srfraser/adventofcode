def find_a_bus_part1(current_time, buses)
  (current_time..).each { |time|
    buses.each { |bus|
      # puts "#{bus} at #{time}, #{time % bus}"
      if time % bus == 0
        return bus * (time - current_time)
      end
    }
  }
end

def find_bus_sequence(buses, start_at = 0)
  bus_count = buses.length
  # Normalise starting location
  if start_at > 0
    start_at = start_at - (start_at % buses[0])
  end
  iterations = 0
  counter = 0
  (start_at..).step(buses[0]).each { |start_time|
    counter += 1
    if counter >= 10000000
      puts "Iteration #{iterations}, currently at timestamp #{start_time}"
      iterations += 1
      counter == 0
    end
    found = (start_time..start_time + bus_count - 1).zip(buses).select { |time, bus|
      # puts "#{time} #{bus}: #{bus == "x" || time % bus == 0}"
      bus == "x" || time % bus == 0
    } # .length

    if found.length == bus_count
      return start_time
    end
  }
end

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Ruby
#def chinese_remainder(mods, remainders)
#  max = mods.inject(:*)
#  series = remainders.zip(mods).map { |r, m| r.step(max, m).to_a }
#  series.inject(:&).first #returns nil when empty
#end
def extended_gcd(a, b)
  last_remainder, remainder = a.abs, b.abs
  x, last_x, y, last_y = 0, 1, 1, 0
  while remainder != 0
    last_remainder, (quotient, remainder) = remainder, last_remainder.divmod(remainder)
    x, last_x = last_x - quotient * x, x
    y, last_y = last_y - quotient * y, y
  end
  return last_remainder, last_x * (a < 0 ? -1 : 1)
end

def invmod(e, et)
  g, x = extended_gcd(e, et)
  if g != 1
    raise "Multiplicative inverse modulo does not exist!"
  end
  x % et
end

def chinese_remainder(mods, remainders)
  max = mods.inject(:*)  # product of all moduli
  series = remainders.zip(mods).map { |r, m| (r * max * invmod(max / m, m) / m) }
  series.inject(:+) % max
end

# x % 17 == 0
# (x+2) % 13 == 0 => x % 13 == 13-2
# (x+3) % 19 == 0 => x % 19 == 19-3

# for all n, find where:
# (t+sequence_pos) % n == 0
def find_bus_sequence_smarter(buses, start_at = 0)
  bus_map = Hash.new
  buses.each_with_index { |bus, index|
    if bus != "x"
      bus_map[bus] = bus - index
    end
  }
  bus_map = bus_map.sort_by { |k, v| -v }.to_h
  bus_numbers = bus_map.keys
  bus_remainders = bus_map.values
  chinese_remainder(bus_numbers, bus_remainders)
end

def process_input(data)
  current_time, buses = data.lines.map(&:chomp).to_a
  current_time = current_time.to_i
  buses = buses.split(",").select { |b| b != "x" }.map(&:to_i)
  [current_time, buses]
end

def process_input_part2(data)
  current_time, buses = data.lines.map(&:chomp).to_a
  current_time = current_time.to_i
  buses.split(",").map { |b|
    if b == "x"
      b
    else
      b.to_i
    end
  }.to_a
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = File.read(input_file)
test_current_time, test_buses = process_input(test_data)
puts "Part 1 test result: #{find_a_bus_part1(test_current_time, test_buses)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = File.read(input_file)
current_time, buses = process_input(real_data)
puts "Part 1 result: #{find_a_bus_part1(current_time, buses)}"

test_data = [
  [[17, "x", 13, 19], 3417, 0],
  [[67, 7, 59, 61], 754018, 700000],
  [[67, "x", 7, 59, 61], 779210, 700000],
  [[67, 7, "x", 59, 61], 1261476, 1100000],
  [[1789, 37, 47, 1889], 1202161486, 1200000000],
]

for buses, result, start in test_data
  puts "Part 2 test result: #{find_bus_sequence_smarter(buses, start)} == #{result}"
end

buses = process_input_part2(real_data)
puts "Part 2 result: #{find_bus_sequence_smarter(buses, 100000000000000)}"
