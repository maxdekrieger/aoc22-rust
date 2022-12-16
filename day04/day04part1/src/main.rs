use std::io::{BufRead, BufReader};
use std::fs::File;
use std::env;
use std::collections::HashSet;

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

    let mut amount_overlapping = 0;

    for line in lines {
        let replaced_line = line.replace(",", "-");
        let mut split = replaced_line.split("-");
        let (str1, str2, str3, str4) = (split.next().unwrap(), split.next().unwrap(), split.next().unwrap(), split.next().unwrap());

        let vec1: Vec<i32> = (str1.parse::<i32>().unwrap() .. str2.parse::<i32>().unwrap() + 1).collect();
        let vec2: Vec<i32> = (str3.parse::<i32>().unwrap() .. str4.parse::<i32>().unwrap() + 1).collect();

        let set1 : HashSet<i32> = HashSet::from_iter(vec1.iter().cloned());
        let set2 : HashSet<i32> = HashSet::from_iter(vec2.iter().cloned());

        let union : HashSet<i32> = set1.union(&set2).cloned().collect();

        if union.eq(&set1) || union.eq(&set2) {
            amount_overlapping += 1;
        }
    }

    println!("{}", amount_overlapping);
}
