

fn part1(data: &mut Vec<i32>) -> i32 {
    let mut steps = 0;
    let mut current_index: i32 = 0;
    let max_index = data.len();
    let mut prev_index: usize;

    while 0 <= current_index && current_index < max_index as i32 {
        prev_index = current_index as usize;
        current_index = current_index + data[current_index as usize];
        data[prev_index] += 1;
        steps += 1;
    }
    steps
}

fn part2(data: &mut Vec<i32>) -> i32 {
    let mut steps = 0;
    let mut current_index: i32 = 0;
    let max_index = data.len();
    let mut prev_index: usize;

    while 0 <= current_index && current_index < max_index as i32 {
        prev_index = current_index as usize;
        current_index = current_index + data[current_index as usize];
        if data[prev_index] >= 3 {
            data[prev_index] -= 1;
        } else {
            data[prev_index] += 1;
        }

        steps += 1;
    }
    steps
}



fn main() {

    let contents = include_str!("../../input");

    let mut data: Vec<i32> = contents.lines().map(|s| s.parse().unwrap()).collect();

    // println!("{:?}", data);

    let mut part2_data = data.clone();
    let part1_result = part1(&mut data);
    println!("Part 1 steps: {}", part1_result);
    let part2_result = part2(&mut part2_data);
    println!("Part 2 steps: {}", part2_result);
}
