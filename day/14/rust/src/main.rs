use std::collections::HashSet;


fn main() {
    let contents = "hfdlxzhv";

    part2(&contents);
}

fn part2(contents: &str) {
    let grid: Vec<Vec<u32>> = (0..128)
        .map(|i| format!("{}-{}", contents, i))
        .map(|d| knothash(&d))
        .collect();

    let regions = part2_scan(grid);
    println!("Found {} regions", regions);
}


fn find_starting_one(grid: &Vec<Vec<u32>>) -> Option<(usize, usize)> {
    for y in 0..128 {
        for x in 0..128 {
            if grid[y][x] == 1 {
                return Some((x, y));
            }
        }
    }
    None
}

fn part2_scan(mut grid: Vec<Vec<u32>>) -> i32 {
    let mut found_regions = 0;
    let size = 128;
    let mut seen = HashSet::with_capacity(size * size);

    println!(
        "Sanity! grid is {} long, grid[0] is {} long",
        grid.len(),
        grid[0].len()
    );
    loop {
        let mut to_scan: Vec<(usize, usize)> = Vec::new();
        let coords = match find_starting_one(&grid) {
            Some(coords) => coords,
            None => break,
        };
        to_scan.push(coords);
        while let Some(current) = to_scan.pop() {
            seen.insert(current);
            let (x, y) = current;
            if grid[y][x] == 0 {
                continue;
            }
            grid[y][x] = 0;
            let mut adj: Vec<(usize, usize)> = current
                .adjacent(size)
                .into_iter()
                .filter(|c| !seen.contains(c))
                .collect();
            to_scan.append(&mut adj);
        }
        found_regions += 1;
    }
    found_regions
}

trait Pos: Sized {
    fn adjacent(&self, limit: usize) -> Vec<Self>;
}

impl Pos for (usize, usize) {
    fn adjacent(&self, limit: usize) -> Vec<Self> {
        let mut rv = Vec::with_capacity(4);
        let l = limit - 1;
        if self.0 < l {
            rv.push((self.0 + 1, self.1));
        }
        if self.1 < l {
            rv.push((self.0, self.1 + 1));
        }
        if self.0 > 0 {
            rv.push((self.0 - 1, self.1));
        }
        if self.1 > 0 {
            rv.push((self.0, self.1 - 1));
        }
        rv
    }
}

fn knothash(contents: &str) -> Vec<u32> {
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

    let output: Vec<u32> = dhash
        .iter()
        .map(|s| format!("{:08b}", s))
        .collect::<Vec<String>>()
        .join("")
        .chars()
        .map(|s| s.to_digit(10).unwrap())
        .collect();
    // println!("{:?}", output);
    output
}


fn reverse(data: &mut Vec<i32>, position: usize, length: usize) {

    let mut subvec: Vec<i32> = data.iter()
        .cycle()
        .skip(position)
        .take(length)
        .map(|s| s.clone())
        .collect();

    subvec.reverse();

    let sublen = data.len();
    for (mut i, item) in (position..).zip(subvec) {
        i = i % sublen;
        data[i] = item;
    }
}
