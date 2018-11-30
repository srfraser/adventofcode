use std::env;
use std::io;
use std::fs::File;
use std::io::prelude::*;

fn count_valid(data: &String) -> i32 {
    let mut total = 0;
    for line in data.lines() {
        let mut data2: Vec<String> = line.split_whitespace().map(|s| s.to_string()).collect();
        let start_size = data2.len();
        data2.sort();
        data2.dedup();
        if start_size == data2.len() {
            total += 1;
        }
        // println!("{:?}", data2);
    }
    total
}

fn count_valid_anagrams(data: &String) -> i32 {
    let mut total = 0;
    for line in data.lines() {
        let mut data2: Vec<String> = line.split_whitespace()
            .map(|s| s.to_string())
            .map(|s| {
                let mut chars: Vec<char> = s.chars().collect();
                chars.sort();
                chars.dedup();
                return chars.into_iter().collect();
            })
            .collect();
        let start_size = data2.len();
        data2.sort();
        data2.dedup();
        if start_size == data2.len() {
            total += 1;
        }
        // println!("{:?}", data2);
    }
    total
}



fn read_file(filename: String) -> Result<(), io::Error> {

    let mut file = File::open(filename)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    println!(
        "Valid entries (duplicates only): {}",
        count_valid(&contents)
    );
    println!(
        "Valid entries (duplicates only): {}",
        count_valid_anagrams(&contents)
    );
    Ok(())
}

fn main() {

    if let Some(arg1) = env::args().nth(1) {
        let result = read_file(arg1);
        match result {
            Ok(v) => println!("Result: {:?}", v),
            Err(e) => println!("error opening file: {:?}", e),
        }
    }
}
