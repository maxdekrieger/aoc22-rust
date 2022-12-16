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

    let alphabet: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".chars().collect();

    let mut sum = 0;

    for line in lines {
        let chars = line.chars();
        let (c1_string, c2_string) = line.split_at(chars.count() / 2);
        let (c1, c2) : (HashSet<char>,HashSet<char>)  = (c1_string.chars().collect(), c2_string.chars().collect());

        for &x in c1.intersection(&c2) {
            let i = alphabet.iter().position(|&a| a == x).unwrap();
            sum += i + 1;
        }
    }

    println!("{}", sum);
}
