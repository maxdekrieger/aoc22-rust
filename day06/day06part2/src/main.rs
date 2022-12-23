use std::io::{BufRead, BufReader};
use std::fs::File;
use std::env;
use std::collections::HashSet;
use std::iter::FromIterator;

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

    let mut chars : Vec<char> = Vec::new();
    let mut result = 0;

    for c in lines.get(0).unwrap().chars() {
        if chars.len() == 14 {
            chars.remove(0);
        }

        result += 1;
        chars.push(c);

        if chars.len() == 14 && HashSet::<char>::from_iter(chars.iter().cloned()).len() == 14 {
            break;
        }
    }

    println!("{}", chars.iter().collect::<String>());

    println!("{}", result);
}
