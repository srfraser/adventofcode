extern crate itertools;

use itertools::FoldWhile::{Continue, Done};
use itertools::Itertools;
use std::collections::HashSet;

fn part1(modifiers: &Vec<i32>) {
    let frequency = modifiers.iter().fold(0, |frequency, m| frequency + m);
    println!("Part 1: {}", frequency);
}

fn part2(modifiers: &Vec<i32>) {
    let mut seen = HashSet::new();
    let frequency = modifiers
        .iter()
        .cycle()
        .fold_while(0, |frequency, m| {
            let result = frequency + m;
            if seen.contains(&result) {
                Done(result)
            } else {
                seen.insert(result);
                Continue(result)
            }
        }).into_inner();

    println!("Part 2: {}", frequency);
}

fn main() {
    let contents = include_str!("../../input");

    let modifiers: Vec<i32> = contents.lines().map(|s| s.parse().unwrap()).collect();

    // println!("{:?}", modifiers);

    part1(&modifiers);

    part2(&modifiers);
}
