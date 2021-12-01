fn main() {
    let lines: Vec<u32> = include_str!("../input.txt")
        .split("\n")
        .map(|l| l.trim().parse().unwrap())
        .collect();

    dbg!(part1(&lines));
    dbg!(part2(&lines));
}

fn part1(lines: &[u32]) -> u32 {
    let mut res = 0;
    for i in 1..lines.len() {
        if lines[i] > lines[i-1] {
            res += 1;
        }
    }

    res
}

fn part2(lines:&[u32]) -> u32 {
    let mut res = 0;
    let mut last_window = u32::MAX;

    for i in 0..lines.len()-2 {
        let window = lines[i..i+3].iter().sum();
        if window > last_window {
            res += 1;
        }

        last_window = window;
    }

    res
}