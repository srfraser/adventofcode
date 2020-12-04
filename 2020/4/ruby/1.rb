required_fields = [
  "byr",
  "iyr",
  "eyr",
  "hgt",
  "hcl",
  "ecl",
  "pid",
# "cid",
]

def process_passport_data(input)
  input.split("\n\n").map { |u|
    u.gsub!("\n", " ")
    new_u = u.split().map { |e|
      e.split(":")
    }.collect { |k, v| [k, v] }.to_h
  }
end

def validate_byr(entry)
  entry = entry.to_i
  (1920 <= entry) && (entry <= 2002)
end

def validate_iyr(entry)
  entry = entry.to_i
  (2010 <= entry) && (entry <= 2020)
end

def validate_eyr(entry)
  entry = entry.to_i
  (2020 <= entry) && (entry <= 2030)
end

def validate_hgt_cm(height)
  height = height.to_i
  (150 <= height) && (height <= 193)
end

def validate_hgt_in(height)
  height = height.to_i
  (59 <= height) && (height <= 76)
end

def validate_hgt(entry)
  if entry.end_with?("cm")
    return validate_hgt_cm(entry.delete("cm"))
  elsif entry.end_with?("in")
    return validate_hgt_in(entry.delete("in"))
  end
  false
end

def validate_hcl(entry)
  entry.match(/^#[0-9a-f]{6}$/)
end

def validate_ecl(entry)
  %W[amb blu brn gry grn hzl oth].include?(entry)
end

def validate_pid(entry)
  entry.match(/^[0-9]{9}$/)
end

def part1(data, required_fields)
  data.select { |d|
    (required_fields - d.keys).empty?
  }.length
end

def part2(data, required_fields)
  validators = {
    :byr => method(:validate_byr).to_proc,
    :iyr => method(:validate_iyr).to_proc,
    :eyr => method(:validate_eyr).to_proc,
    :hgt => method(:validate_hgt).to_proc,
    :hcl => method(:validate_hcl).to_proc,
    :ecl => method(:validate_ecl).to_proc,
    :pid => method(:validate_pid).to_proc,
  }
  valid_first_pass = data.select { |d|
    (required_fields - d.keys).empty?
  }
  valid_first_pass.select { |entry|
    entry.all? { |k, v|
      if validators.has_key?(k.to_sym)
        validators[k.to_sym].(v)
      else
        true
      end
    }
  }.length
end

input_file = File.join(File.dirname(__FILE__), "../test_input")
test_data = process_passport_data(File.read(input_file))
puts "Test passports valid: #{part1(test_data, required_fields)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = process_passport_data(File.read(input_file))
puts "Part 1 passports valid: #{part1(real_data, required_fields)}"

input_file = File.join(File.dirname(__FILE__), "../test_input_part2_invalid")
test_data = process_passport_data(File.read(input_file))
puts "Test part 2 invalid passports: #{part2(test_data, required_fields)}"

input_file = File.join(File.dirname(__FILE__), "../test_input_part2_valid")
test_data = process_passport_data(File.read(input_file))
puts "Test part 2 valid passports: #{part2(test_data, required_fields)}"

input_file = File.join(File.dirname(__FILE__), "../input")
real_data = process_passport_data(File.read(input_file))
puts "Part passports valid: #{part2(real_data, required_fields)}"
