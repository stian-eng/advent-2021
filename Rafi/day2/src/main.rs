fn main() {
    let lines = include_str!("../input.txt")
        .split("\n")
        .map(|line| {
            let mut split = line.trim().split(" ");
            (split.next().unwrap(), split.next().unwrap().parse::<u32>().unwrap())
        })
        .collect::<Vec<(&str, u32)>>();

    part1(&lines);
    part2(&lines);
}

fn part1(lines: &[(&str, u32)]) {
    let mut horizontal = 0;
    let mut vertical = 0;

    for line in lines {
        match line.0 {
            "forward" => horizontal += line.1,
            "up" => vertical -= line.1,
            "down" => vertical += line.1,
            _ => unreachable!()
        }
    }

    println!("{}", horizontal * vertical)

}

fn part2(lines: &[(&str, u32)]) {
    let mut horizontal = 0;
    let mut vertical = 0;
    let mut aim = 0;

    for line in lines {
        match line.0 {
            "forward" => {
                horizontal += line.1;
                vertical += aim * line.1;
            },
            "up" => aim -= line.1,
            "down" => aim += line.1,
            _ => unreachable!()
        }
    }

    println!("{}", horizontal * vertical)
}
