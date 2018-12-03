extern crate regex;
use regex::Regex;
use std::collections::HashMap;
use std::str::FromStr;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct Coord {
    x: usize,
    y: usize,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Claim {
    start_x: usize,
    start_y: usize,
    size_x: usize,
    size_y: usize,
    claim_id: usize,
}

impl Claim {
    fn new(claim_id: usize, start_x: usize, start_y: usize, size_x: usize, size_y: usize) -> Self {
        Self {
            claim_id: claim_id,
            start_x: start_x,
            start_y: start_y,
            size_x: size_x,
            size_y: size_y,
        }
    }

    fn coords(self) -> Vec<Coord> {
        let mut vec = vec![];
        for x in self.start_x..(self.start_x + self.size_x) {
            for y in self.start_y..(self.start_y + self.size_y) {
                vec.push(Coord { x, y });
            }
        }
        vec
    }

    fn intersects(self, other: Claim) -> bool {
        if self.start_x + self.size_x < other.start_x
            || other.start_x + other.size_x < self.start_x
            || self.start_y + self.size_y < other.start_y
            || other.start_y + other.size_y < self.start_y
        {
            return false;
        } else {
            true
        }
    }

    fn intersects_any(self, others: &Vec<Claim>) -> bool {
        for other in others {
            if self.claim_id == other.claim_id {
                continue;
            }
            if self.intersects(*other) {
                return false;
            }
        }
        true
    }
}

impl FromStr for Claim {
    type Err = ();

    fn from_str(input: &str) -> Result<Self, Self::Err> {
        let re = Regex::new(r"#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)").unwrap();
        let parts: Vec<usize> = re
            .captures(input)
            .unwrap()
            .iter()
            .skip(1) // first capture group is the entire string.
            .map(|i| i.unwrap().as_str().parse::<usize>().unwrap())
            .collect();
        if parts.len() != 5 {
            Err(())
        } else {
            Ok(Self::new(parts[0], parts[1], parts[2], parts[3], parts[4]))
        }
    }
}

fn main() {
    let contents = include_str!("../../input");

    // let test_input = vec!["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"];
    let test_input: Vec<String> = contents.lines().map(|s| s.parse().unwrap()).collect();

    let mut test_claims: Vec<Claim> = test_input
        .iter()
        .map(|c| Claim::from_str(c).unwrap())
        .collect();

    // println!("{:?}", test_claims);

    let mut fabric = HashMap::new();
    for claim in test_claims.iter() {
        for coord in claim.coords() {
            match fabric.get(&coord) {
                Some(&number) => fabric.insert(coord, number + 1),
                _ => fabric.insert(coord, 1),
            };
        }
    }

    let overlaps = fabric.values().filter(|x| **x > 1).count();

    println!("Part 1: {:?}", overlaps);
    let saved_claims = test_claims.to_vec();
    test_claims.retain(|&c| c.intersects_any(&saved_claims));
    println!("Part 2: {:?}", test_claims);
}
