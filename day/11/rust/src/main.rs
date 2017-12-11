use std::collections::HashMap;

#[derive(Debug)]
struct Coord {
    x: i32,
    y: i32,
    z: i32,
}

fn movecoord(start: &mut Coord, direction: &Coord) {
    start.x += direction.x;
    start.y += direction.y;
    start.z += direction.z;
}

fn cube_distance(a: &Coord, b: &Coord) -> i32 {
    ((a.x - b.x).abs() + (a.y - b.y).abs() + (a.z - b.z).abs()) / 2
}



fn part1(contents: &str) {
    let data: Vec<&str> = contents.trim_right().split(',').collect();

    let mut direction_map = HashMap::new();
    direction_map.insert("n", Coord { x: 0, y: 1, z: -1 });
    direction_map.insert("ne", Coord { x: 1, y: 0, z: -1 });
    direction_map.insert("se", Coord { x: 1, y: -1, z: 0 });
    direction_map.insert("s", Coord { x: 0, y: -1, z: 1 });
    direction_map.insert("sw", Coord { x: -1, y: 0, z: 1 });
    direction_map.insert("nw", Coord { x: -1, y: 1, z: 0 });

    let start = Coord { x: 0, y: 0, z: 0 };
    let mut current = Coord { x: 0, y: 0, z: 0 };

    let mut max_distance = 0;
    let mut current_distance: i32;

    for step in data {
        movecoord(&mut current, direction_map.get(step).unwrap());
        current_distance = cube_distance(&start, &current);
        if current_distance > max_distance {
            max_distance = current_distance;
        }
    }
    println!(
        "Position {:?} is {} steps away",
        current,
        cube_distance(&start, &current)
    );
    println!(
        "Furthest point from the start was {} steps away",
        max_distance
    );
}

fn main() {
    let contents = include_str!("../../input");
    part1(&contents);
}
