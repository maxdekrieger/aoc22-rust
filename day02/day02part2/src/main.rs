use std::io::{BufRead, BufReader};
use std::fs::File;
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

    let mut score = 0;

    for line in lines {
        let mut chars = line.chars();
        let opponent_char = chars.next().unwrap();
        let my_char = chars.last().unwrap();

        match my_char {
            'X' => {
                score += 0;
                match opponent_char {
                    'A' => {
                        score += 3
                    }
                    'B' => {
                        score += 1
                    }
                    'C' => {
                        score += 2
                    }
                    _ => {
                        panic!("Unexpected match, opponent char: {}", opponent_char);
                    }
                }
            }
            'Y' => {
                score += 3;
                match opponent_char {
                    'A' => {
                        score += 1
                    }
                    'B' => {
                        score += 2
                    }
                    'C' => {
                        score += 3
                    }
                    _ => {
                        panic!("Unexpected match, opponent char: {}", opponent_char);
                    }
                }
            }
            'Z' => {
                score += 6;
                match opponent_char {
                    'A' => {
                        score += 2
                    }
                    'B' => {
                        score += 3
                    }
                    'C' => {
                        score += 1
                    }
                    _ => {
                        panic!("Unexpected match, opponent char: {}", opponent_char);
                    }
                }
            }
            _ => {
                panic!("Unexpected match, my char: {}", my_char);
            }
        }
    }

    println!("{}", score);
}
