

fn most_blocks(data: &mut Vec<i32>) -> usize {
    data.iter()
        .position(|&r| r == *data.iter().max().unwrap())
        .unwrap()
}


fn redistribute(mut data: &mut Vec<i32>) {
    let mut index = most_blocks(&mut data);
    let mut to_spend = data[index];
    data[index] = 0;

    while to_spend > 0 {
        index += 1;
        index %= data.len();
        to_spend -= 1;
        data[index] += 1;
    }
}

fn main() {
    let contents = include_str!("../../input");
    let mut data: Vec<i32> = contents
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    println!("{:?}", data);

    let mut seen = Vec::new();
    // println!("seen: {:?}", seen.iter().any(|r| *r == data));

    while !seen.iter().any(|r| *r == data) {
        seen.push(data.clone());
        redistribute(&mut data);
        // println!("data: {:?}", data);

    }

    println!("Final value: {:?}", data);
    println!("Cycles until duplicate: {:?}", seen.len());

    let first = seen.iter().position(|r| *r == data).unwrap();
    println!("Distance between duplicates: {:?}", seen.len() - first);
}
