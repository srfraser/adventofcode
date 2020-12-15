def play_memory_game_naively(sequence, desired_number = 2020)
  (1..desired_number).each { |_|
    last_spoken = sequence[-1]
    if sequence[0..-2].include?(last_spoken)
      # puts "#{last_spoken} was in #{sequence[..-2]}"
      sequence.append(sequence.length - 1 - sequence[0..-2].rindex(last_spoken))
    else
      # puts "#{last_spoken} was not in #{sequence[..-2]}"
      sequence.append(0)
    end
  }
  sequence[desired_number - 1]
end

def play_memory_game(sequence, desired_number = 2020)
  index_cache = sequence[0..-2].zip(0..).map { |s, index| [s, index] }.to_h
  next_to_speak = sequence[-1]
  # index_cache.delete!(last_spoken)

  (index_cache.length..desired_number).each { |current_position|
    new_index = 0
    if index_cache.has_key?(next_to_speak)
      new_index = current_position - index_cache[next_to_speak]
    end
    # puts "Saying #{next_to_speak} at #{current_position}, next up is #{new_index}"
    index_cache[next_to_speak] = current_position
    next_to_speak = new_index
  }
  index_cache.select { |k, v|
    v == desired_number - 1
  }.keys[0]
end

part1_tests = [
  [[0, 3, 6], 436, 2020],
  [[1, 3, 2], 1, 2020],
  [[2, 1, 3], 10, 2020],
  [[1, 2, 3], 27, 2020],
  [[2, 3, 1], 78, 2020],
  [[3, 2, 1], 438, 2020],
  [[3, 1, 2], 1836, 2020],
]
for input, expected, desired in part1_tests
  puts "Part 1 test #{play_memory_game(input, desired)} == #{expected}"
end

puts "Part 1 actual #{play_memory_game([11, 0, 1, 10, 5, 19])}"

part2_tests = [
  [[0, 3, 6], 175594, 30000000],
  [[1, 3, 2], 2578, 30000000],
  [[2, 1, 3], 3544142, 30000000],
  [[1, 2, 3], 261214, 30000000],
  [[2, 3, 1], 6895259, 30000000],
  [[3, 2, 1], 18, 30000000],
  [[3, 1, 2], 362, 30000000],
]
for input, expected, desired in part2_tests
  puts "Part 2 test #{play_memory_game(input, desired)} == #{expected}"
end

puts "Part 2 actual #{play_memory_game([11, 0, 1, 10, 5, 19], 30000000)}"
