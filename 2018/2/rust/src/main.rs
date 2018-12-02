extern crate counter;
extern crate itertools;
use counter::Counter;

use itertools::Itertools;

fn exactly(data: String, count: usize) -> bool {
    let mut char_counts = data.chars().collect::<Counter<_>>();
    char_counts.retain(|&_k, &mut v| v == count);
    if char_counts.keys().len() > 0 {
        return true;
    }
    return false;
}

fn part1(boxids: &Vec<String>) {
    let twos = boxids
        .iter()
        .filter(|s| exactly(s.to_string(), 2))
        .collect::<Vec<&String>>()
        .len();
    let threes = boxids
        .iter()
        .filter(|s| exactly(s.to_string(), 3))
        .collect::<Vec<&String>>()
        .len();
    println!("Part 1: {:?}", twos * threes);
}

fn charmatch(s1: &String, s2: &String) -> bool {
    // let mut differences = 0;
    let differences = s1.chars().zip(s2.chars()).fold(0, |differences, a| {
        if a.0 != a.1 {
            differences + 1
        } else {
            differences
        }
    });
    if differences != 1 {
        return false;
    }
    return true;
}

fn part2(boxids: &Vec<String>) {
    for combo in boxids.iter().combinations(2) {
        if charmatch(combo[0], combo[1]) {
            println!("Part 2: {:?}", combo);
        }
    }
}

fn main() {
    let contents = include_str!("../../input");

    let boxids: Vec<String> = contents.lines().map(|s| s.parse().unwrap()).collect();

    // println!("{:?}", boxids);

    part1(&boxids);

    part2(&boxids);
}
