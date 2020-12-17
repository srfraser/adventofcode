class Cube
  def initialize(coord, state)
    @dimensions = coord.length
    if coord.length == 3
      @x, @y, @z = coord
    else
      @x, @y, @z, @w = coord
    end

    if state == "#" || state == true
      @active = true
    else
      @active = false
    end
    @next_state = @active
  end

  def is_active?
    @active
  end

  def str
    if @active
      "#"
    else
      "."
    end
  end

  def neighbours
    if @dimensions == 3
      neighbours_3d()
    else
      neighbours_4d()
    end
  end

  def neighbours_3d
    n = [@x - 1, @x, @x + 1].product([@y - 1, @y, @y + 1], [@z - 1, @z, @z + 1])
    n.delete([@x, @y, @z])
    n
  end

  def neighbours_4d
    n = [@x - 1, @x, @x + 1].product([@y - 1, @y, @y + 1], [@z - 1, @z, @z + 1], [@w - 1, @w, @w + 1])
    n.delete([@x, @y, @z, @w])
    n
  end

  def set_next(state)
    @next_state = state
  end

  def update_state
    @active = @next_state
  end
end

def process_input_file(filename)
  contents = File.read(filename)
  # all on plane to start with
  z = 0
  contents.lines.map(&:chomp).zip(0..).map { |line, y|
    line.split("").zip(0..).map { |c, x|
      # puts "Assigning #{[x, y, z]} to #{c}"
      [[x, y, z], Cube.new([x, y, z], c)]
    }
  }.flatten(1).to_h
end

def process_input_file_4d(filename)
  contents = File.read(filename)
  # all on plane to start with
  z = 0
  w = 0
  contents.lines.map(&:chomp).zip(0..).map { |line, y|
    line.split("").zip(0..).map { |c, x|
      [[x, y, z, w], Cube.new([x, y, z, w], c)]
    }
  }.flatten(1).to_h
end

def count_active_neighbours(coords, grid)
  grid[coords].neighbours.select { |n| grid.include?(n) && grid[n].is_active? }.length
end

def add_neighbours(grid)
  all_neighbour_spaces = grid.map { |coord, cube| cube.neighbours }.flatten(1)
  all_neighbour_spaces.each { |coord|
    if !grid.include?(coord)
      grid[coord] = Cube.new(coord, ".")
    end
  }
  grid
end

def display_grid(grid)
  used_x, used_y, used_z = grid.keys.transpose

  (used_z.min..used_z.max).each { |z|
    puts "z=#{z}"
    (used_y.min..used_y.max).each { |y|
      (used_x.min..used_x.max).each { |x|
        if !grid.include?([x, y, z])
          print "."
        else
          print grid[[x, y, z]].str
        end
      }
      print "\n"
    }
  }
end

def alive_cubes(grid, iterations)
  # display_grid(grid)
  (1..iterations).each { |iteration|
    grid = add_neighbours(grid)
    # puts "#{iteration}, grid has #{grid.length} entries"
    grid.each { |coord, cube|
      active_neighbours = count_active_neighbours(coord, grid)
      if cube.is_active? && !(active_neighbours == 2 || active_neighbours == 3)
        cube.set_next(false)
      elsif !cube.is_active? && active_neighbours == 3
        cube.set_next(true)
      end
    }
    grid.each { |coord, cube|
      cube.update_state
    }
    # display_grid(grid)
  }
  grid.select { |coord, cube| cube.is_active? }.length
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = process_input_file(input_file)
puts "Part 1 test result: #{alive_cubes(test_data, 6)} == 112"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = process_input_file(input_file)
puts "Part 1 result: #{alive_cubes(real_data, 6)}"

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = process_input_file_4d(input_file)
puts "Part 2 test result: #{alive_cubes(test_data, 6)} == 848"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = process_input_file_4d(input_file)
puts "Part 2 result: #{alive_cubes(test_data, 6)}"
