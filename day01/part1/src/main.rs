use std::io::{BufRead, BufReader};
use std::fs::File;
use std::cmp;

fn main() {
    // let filename = "data/input-test.txt";
    let filename = "data/input.txt";

    let reader = BufReader::new(File::open(filename).expect(&format!("Cannot open {}", filename)));
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
