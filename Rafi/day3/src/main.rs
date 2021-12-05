

fn main() {
    let lines = include_str!("../input.txt")
        .split("\n")
        .map(|str| str.trim().chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    part1(&lines);
    part2(&lines);
}


fn part1(lines: &Vec<Vec<char>>) {
    let n_bits = lines[0].len();
    let n_lines = lines.len();

    let mut ones = vec![0; n_bits];

    for i in 0..n_bits {
        for line in lines {
            if line[i] == '1' {
                ones[i] += 1;
            }
        }
    }

    let gamma = ones.iter()
        .map(|count| match *count > (n_lines / 2) {
            true => "1",
            false => "0",
        }).
        collect::<String>();

    let gamma = isize::from_str_radix(&gamma, 2).unwrap();

    let eps = ones.iter()
        .map(|count| match *count > (n_lines / 2) {
            true => "0",
            false => "1",
        }).
        collect::<String>();

    let eps = isize::from_str_radix(&eps, 2).unwrap();

    println!("{}", gamma * eps);
}

fn part2(lines: &Vec<Vec<char>>) {
    let n_bits = lines[0].len();

    let mut ox_candidates = lines.clone();
    let mut co_candidates = lines.clone();

    let mut ox_result = 0;
    let mut co_result = 0;

    for i in 0..n_bits {
        let mut ox_ones = 0;
        for line in &ox_candidates {
            if line[i] == '1' {
                ox_ones += 1;
            }
        }

        let mut co_ones = 0;
        for line in &co_candidates {
            if line[i] == '1' {
                co_ones += 1;
            }
        }

        let ox_target = match ox_ones as f64 >= (ox_candidates.len() as f64 / 2f64) {
            true => '1',
            false => '0',
        };

        ox_candidates = keep_targets(ox_candidates, i, ox_target);

        if ox_candidates.len() == 1 {
            let collected: String = ox_candidates[0].iter().collect();
            ox_result = isize::from_str_radix(collected.as_str(), 2).unwrap();
        }

        let co2_target = match co_ones as f64 >= (co_candidates.len() as f64 / 2f64) {
            true => '0',
            false => '1',
        };

        co_candidates = keep_targets(co_candidates, i, co2_target);

        if co_candidates.len() == 1 {
            let collected: String = co_candidates[0].iter().collect();
            co_result = isize::from_str_radix(collected.as_str(), 2).unwrap();
        }
    }

    println!("{}", ox_result * co_result);
}

fn keep_targets(lines: Vec<Vec<char>>, i: usize, target: char) -> Vec<Vec<char>>{
    lines.into_iter().filter(|line| {
        line[i] == target
    })
    .collect()
}