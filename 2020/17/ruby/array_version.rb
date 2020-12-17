require "set"

$cache = Hash.new
$cache[3] = Hash.new
$cache[4] = Hash.new

def neighbours_old(coord, dimensions)
  if dimensions == 3
    neighbours_3d(coord)
  else
    neighbours_4d(coord)
  end
end

def neighbours(coord, dimensions)
  if !$cache[dimensions].has_key?(coord)
    if dimensions == 3
      $cache[dimensions][coord] = neighbours_3d(coord)
    else
      $cache[dimensions][coord] = neighbours_4d(coord)
    end
  end
  return $cache[dimensions][coord]
end

def neighbours_3d(coord)
  x, y, z = coord
  n = [x - 1, x, x + 1].product([y - 1, y, y + 1], [z - 1, z, z + 1])
  n.delete([x, y, z])
  n
end

def neighbours_4d(coord)
  x, y, z, w = coord
  n = [x - 1, x, x + 1].product([y - 1, y, y + 1], [z - 1, z, z + 1], [w - 1, w, w + 1])
  n.delete([x, y, z, w])
  n
end

def process_input_file(filename)
  contents = File.read(filename)
  # all on plane to start with
  z = 0
  contents.lines.map(&:chomp).zip(0..).map { |line, y|
    line.split("").zip(0..).map { |c, x|
      if c == "#"
        [x, y, z]
      end
    }
  }.flatten(1).select { |coord| coord != nil }
end

def process_input_file_4d(filename)
  contents = File.read(filename)
  # all on plane to start with
  z = 0
  w = 0
  contents.lines.map(&:chomp).zip(0..).map { |line, y|
    line.split("").zip(0..).map { |c, x|
      if c == "#"
        [x, y, z, w]
      end
    }
  }.flatten(1).select { |coord| coord != nil }
end

def count_active_neighbours(coord, grid, dimensions)
  # neighbours(coord, dimensions).select { |c| grid.include?(c) }.length
  sum = 0
  neighbours(coord, dimensions).each { |c|
    if grid.include?(c)
      sum += 1
    end
  }
  sum
end

def all_neighbours(grid, dimensions)
  grid.map { |coord| neighbours(coord, dimensions) }.flatten(1).to_set.to_a
end

def display_grid(grid)
  used_x, used_y, used_z = grid.transpose

  (used_z.min..used_z.max).each { |z|
    puts "z=#{z}"
    (used_y.min..used_y.max).each { |y|
      (used_x.min..used_x.max).each { |x|
        if !grid.include?([x, y, z])
          print "."
        else
          print "#"
        end
      }
      print "\n"
    }
  }
end

def alive_cubes(grid, dimensions, iterations)
  # display_grid(grid)
  (1..iterations).each { |iteration|
    next_grid = Array.new
    all_spaces = (all_neighbours(grid, dimensions) + grid).to_set.to_a
    puts "Looking at #{all_spaces.length} potential spaces"

    all_spaces.each { |coord|
      active_neighbours = count_active_neighbours(coord, grid, dimensions)
      if grid.include?(coord)
        if active_neighbours == 2 || active_neighbours == 3
          next_grid.append(coord)
        end
      elsif !grid.include?(coord) && active_neighbours == 3
        next_grid.append(coord)
      end
    }
    grid = next_grid
    puts "active cells = #{grid.length}"
    # display_grid(grid)
  }
  grid.length
end

#input_file = File.join(File.dirname(__FILE__), "../test_input")
#test_data = process_input_file(input_file)
#puts "Part 1 test result: #{alive_cubes(test_data, 3, 6)} == 112"

#input_file = File.join(File.dirname(__FILE__), "../input")
#real_data = process_input_file(input_file)
#puts "Part 1 result: #{alive_cubes(real_data, 3, 6)}"

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = process_input_file_4d(input_file)
puts "Part 2 test result: #{alive_cubes(test_data, 4, 6)} == 848"

#input_file = File.join(File.dirname(__FILE__), "../input")
#real_data = process_input_file_4d(input_file)
# puts "Part 2 result: #{alive_cubes(real_data, 4, 6)}"
