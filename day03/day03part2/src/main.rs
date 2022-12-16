use core::panic;
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
    let mut group : Vec<HashSet<char>> = Vec::new();

    for line in lines {
        group.push(line.chars().collect());

        if group.len() == 3 {
            let intersection = group.iter().skip(1).fold(
                group[0].clone()
                , |acc, hs| {
                    acc.intersection(hs).cloned().collect()
                });

            if intersection.len() != 1 {
                panic!("Intersection is more than one: {:?}", intersection);
            }

            let &badge = intersection.iter().next().unwrap();
            sum += alphabet.iter().position(|&a| a == badge).unwrap() + 1;

            group.clear();
        }
    }

    println!("{}", sum);
}
