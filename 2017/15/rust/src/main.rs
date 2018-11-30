fn main() {
    part1();
    part2();
}

struct Generator {
    factor: u64,
    current: u64,
    remainder: u64,
}

impl Iterator for Generator {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        loop {
            self.current = (self.current * self.factor) % 2147483647;
            if self.current % self.remainder == 0 {
                break;
            }
        }
        Some(self.current as u32)
    }
}

fn make_generator(seed: u64, factor: u64, remainder: u64) -> Generator {
    Generator {
        current: seed,
        factor: factor,
        remainder: remainder,
    }
}



fn part1() {
    let mut total = 0;

    for i in make_generator(116, 16807, 1)
        .zip(make_generator(299, 48271, 1))
        .take(40000000)
    {
        if i.0 & 0xFFFF == i.1 & 0xFFFF {
            total += 1;
        }
    }
    println!("Part 1 found {:?} matches", total);
}

fn part2() {
    let mut total = 0;

    for i in make_generator(116, 16807, 4)
        .zip(make_generator(299, 48271, 8))
        .take(5000000)
    {
        if i.0 & 0xFFFF == i.1 & 0xFFFF {
            total += 1;
        }
    }
    println!("Part 2 found {:?} matches", total);
}
