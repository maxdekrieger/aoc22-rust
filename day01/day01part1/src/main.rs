use std::io::{BufRead, BufReader};
use std::fs::File;
use std::cmp;
use std::env;

fn main() {
    let mut input = env::current_exe().unwrap();
    input.pop();
    input.pop();
    input.pop();
    input.push("data");
    input.push("input.txt");
    // input.push("input-test.txt");

    let reader = BufReader::new(File::open(&input).expect(&format!("Cannot open {}", input.display())));
    let lines : Vec<String> = reader.lines().map(|l| l.expect("Could not parse line")).collect();

    let mut max_calories = 0;
    let mut cur_calories = 0;

    for line in lines {
        if line.is_empty() {
            max_calories = cmp::max(max_calories, cur_calories);
            cur_calories = 0;
            continue;
        }

        cur_calories += line.parse::<i32>().unwrap();
    }

    max_calories = cmp::max(max_calories, cur_calories);

    println!("{}", max_calories)
}
