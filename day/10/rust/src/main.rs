fn main() {
    let contents = include_str!("../../input");

    part1(&contents);
    part2(&contents);
}


fn part1(contents: &str) {

    let data: Vec<i32> = contents
            .lines()
            .next()
            .unwrap()  // bloody newlines
            .split(',')
            .map(|s| s.parse().unwrap())
            .collect();
    let mut current_position = 0;
    let mut skip_size = 0;
    let mut circle: Vec<i32> = (0..256).collect();

    for length in data {
        reverse(&mut circle, current_position as usize, length as usize);
        current_position = (current_position + length + skip_size) % circle.len() as i32;
        skip_size += 1;
    }
    println!("Product of first two elements: {}", circle[0] * circle[1]);
}


fn part2(contents: &str) {
    let mut data: Vec<i32> = contents
        .lines()
        .next()
        .unwrap()
        .chars()
        .map(|s| s as i32)
        .collect();

    data.extend(vec![17, 31, 73, 47, 23]);

    let mut current_position = 0;
    let mut skip_size = 0;
    let mut circle: Vec<i32> = (0..256).collect();

    for _ in 0..64 {
        for length in &data {
            reverse(&mut circle, current_position as usize, *length as usize);
            current_position = (current_position + *length + skip_size) % circle.len() as i32;
            skip_size += 1;
        }
    }

    let mut dhash: Vec<i32> = Vec::new();
    for chunk in circle.chunks(16) {
        dhash.push(chunk.iter().fold(0, |acc, &x| acc ^ x));
    }
    let output = dhash
        .iter()
        .map(|s| format!("{:x}", s))
        .collect::<Vec<_>>()
        .join("");
    println!("Hash: {:?}", output);
}



fn reverse(data: &mut Vec<i32>, position: usize, length: usize) {
    // let mut subvec = Vec::new();

    let mut subvec: Vec<i32> = data.iter()
        .cycle()
        .skip(position)
        .take(length)
        .map(|s| s.clone())
        .collect();
    // for item in data.iter().cycle().skip(position).take(length) {
    //    subvec.push(item.clone());
    // }
    subvec.reverse();

    let sublen = data.len();
    for (mut i, item) in (position..).zip(subvec) {
        i = i % sublen;
        data[i] = item;
    }
}
