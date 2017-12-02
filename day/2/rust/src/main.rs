use std::env;
use std::io;
use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;

fn checksum(data: &mut [i32]) -> Result<i32, String> {
    let max = try!(data.iter().max().ok_or("No max"));
    let min = try!(data.iter().min().ok_or("No min"));
    Ok(max - min)
}


fn find_quotient(data: &mut [i32]) -> Result<i32, String> {
    for first in 0..data.len() {
        for second in first + 1..data.len() {
            let tuple = [data[first], data[second]];
            let max = try!(tuple.iter().max().ok_or("No max"));
            let min = try!(tuple.iter().min().ok_or("No min"));
            if max % min == 0 {
                return Ok(max / min);
            }
        }
    }
    Ok(0)
}

fn read_file(filename: String) -> Result<(), io::Error> {
    let f = try!(File::open(filename));
    let file = BufReader::new(&f);
    let mut checksum_total = 0;
    let mut quotient_total = 0;
    for line in file.lines() {
        let mut data: Vec<i32> = line.unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        // println!("{:?}", data);
        let checksum = checksum(data.as_mut_slice());
        match checksum {
            Ok(v) => checksum_total = checksum_total + v,
            Err(e) => println!("No checksum {}", e),
        }
        let quotient = find_quotient(data.as_mut_slice());
        match quotient {
            Ok(v) => quotient_total = quotient_total + v,
            Err(e) => println!("No sane division found {}", e),
        }
    }
    println!("Checksum total: {}", checksum_total);
    println!("Found quotient total: {}", quotient_total);

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
