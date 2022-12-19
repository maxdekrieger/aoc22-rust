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
    
    let mut stacks : Vec<Vec<char>> = Vec::new();

    for line in &lines {
        if !line.contains("[") {
            let amount : i32 = line.split_whitespace().last().unwrap().trim().parse().unwrap();
            println!("{} stacks", amount);
            for _ in 0 .. amount {
                stacks.push(Vec::new())
            }
            break;
        }
    }


    // build structure
    for line in &lines {
        if line.contains("[") {
            for i in 0 .. stacks.len() {
                let c = line.chars().nth(1 + 4*i).unwrap();
                if !c.is_whitespace() {
                    stacks.get_mut(i).unwrap().push(c);
                }
            }
        } else if line.is_empty() {
            break;
        }
    }

    // reverse stacks
    let mut reversed_stacks : Vec<Vec<char>> = Vec::new();
    for mut s in stacks {
        s.reverse();
        reversed_stacks.push(s);
    }

    // {
    //     let mut i = 1;
    //     for s in &reversed_stacks {
    //         println!("Stack {}: {}", i, s.iter().collect::<String>());
    //         i += 1;
    //     }
    //     println!();
    // }

    for mut line in lines {
        if line.contains("move") {
            line = line.replace("move ", "");
            line = line.replace("from ", "");
            line = line.replace("to ", "");
            let mut split = line.split(" ");
            let (n, from_idx, to_idx) : (usize, usize, usize) = (split.next().unwrap().parse().unwrap(), split.next().unwrap().parse().unwrap(), split.next().unwrap().parse().unwrap());

            let from = reversed_stacks.get_mut(from_idx - 1).unwrap();
            let mut popped : Vec<char> = Vec::new();
            for _ in 0 .. n {
                let c = from.pop().unwrap();
                popped.push(c);
            }
            popped.reverse();

            let to = reversed_stacks.get_mut(to_idx - 1).unwrap();
            for c in popped {
                to.push(c);
            }

            // let mut i = 1;
            // for s in &reversed_stacks {
            //     println!("Stack {}: {}", i, s.iter().collect::<String>());
            //     i += 1;
            // }
            // println!();
        }
    }

    let mut result : Vec<char> = Vec::new();
    for s in &reversed_stacks {
        result.push(*s.iter().last().unwrap());
    }
    println!("{}", result.iter().collect::<String>());
}
