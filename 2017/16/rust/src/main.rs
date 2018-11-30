

#[derive(Debug)]
struct Troupe {
    troupe: Vec<char>,
}

impl Default for Troupe {
    fn default() -> Troupe {
        Troupe { troupe: (0..16).map(|x| (x + 'a' as u8) as char).collect::<Vec<_>>() }
    }
}

impl Troupe {
    fn spin(&mut self, count: usize) {
        let length = self.troupe.len();
        let skip_to = length - count;

        self.troupe = self.troupe
            .iter()
            .cycle()
            .skip(skip_to)
            .take(length)
            .map(|s| s.clone())
            .collect();
    }
    fn exchange(&mut self, index1: usize, index2: usize) {
        self.troupe.swap(index1, index2);
    }
    fn partner(&mut self, name1: char, name2: char) {
        let pos1 = self.troupe.iter().position(|&r| r == name1).unwrap();
        let pos2 = self.troupe.iter().position(|&r| r == name2).unwrap();
        self.exchange(pos1, pos2);
    }
    fn show(&self) -> String {
        self.troupe
            .iter()
            .map(|c| c.to_string())
            .collect::<String>()
    }
}


fn part1(raw_moves: &str, t: &mut Troupe) {
    for s in raw_moves.split(",") {
        match s.chars().next() {
            Some('s') => {
                let spincount = &s[1..].parse::<usize>().unwrap();
                t.spin(*spincount);
            }
            Some('x') => {
                let indeces: Vec<usize> = s[1..]
                    .split("/")
                    .map(|i| i.parse::<usize>().unwrap())
                    .collect();
                t.exchange(indeces[0], indeces[1])
            }
            Some('p') => {
                let names: Vec<char> = s[1..]
                    .split("/")
                    .take(2)
                    .map(|s| s.chars().next().unwrap())
                    .collect();
                t.partner(names[0], names[1])
            }
            Some(_) => {}
            None => {}
        };
    }
}

fn main() {
    let raw_moves = include_str!("../../input").trim_matches('\n');

    let mut t: Troupe = Troupe { ..Default::default() };
    println!("Start: {:?}", t.show());

    part1(&raw_moves, &mut t);

    println!("Part 1: {:?}", t.show());

}
