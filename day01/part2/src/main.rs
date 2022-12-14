use std::io::{BufRead, BufReader};
use std::fs::File;

fn main() {
    // let filename = "data/input-test.txt";
    let filename = "data/input.txt";

    let reader = BufReader::new(File::open(filename).expect(&format!("Cannot open {}", filename)));
    let lines : Vec<String> = reader.lines().map(|l| l.expect("Could not parse line")).collect();

    let mut all_calories = Vec::new();
    let mut cur_calories = 0;

    for line in lines {
        if line.is_empty() {
            all_calories.push(cur_calories);
            cur_calories = 0;
            continue;
        }

        cur_calories += line.parse::<i32>().unwrap();
    }
    all_calories.push(cur_calories);
    
    all_calories.sort_by(|a,b| b.cmp(a));
    let top_3 = all_calories[0] + all_calories[1] + all_calories[2];

    println!("{}", top_3);
}
