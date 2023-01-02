use std::io::{BufRead, BufReader};
use std::fs::File;
use std::env;
use std::collections::HashMap;

#[derive(Debug,Clone)]
struct ElvenFile {
    name: String,
    size: u64
}


impl ElvenFile {
    pub fn new(name: String, size: u64) -> Self {
        Self {
            name,
            size,
        }
    }
}

#[derive(Debug,Clone)]
struct ElvenDirectory {
    name: String,
    parent: Option<String>,

    directories: Vec<String>,
    files: Vec<ElvenFile>,

    size: Option<u64>
}


impl ElvenDirectory {
    pub fn new(name: String, parent: Option<String>) -> Self {
        Self {
            name,
            parent,

            files: Vec::new(),
            directories: Vec::new(),

            size: None
        }
    }

    pub fn get_size(&self, efs: &HashMap<String, ElvenDirectory>) -> (u64, Option<ElvenDirectory>) {
        if self.size.is_some() {
            return (self.size.unwrap(), None);
        }

        let mut size: u64 = 0;
        for d in &self.directories {
            size += efs.get(d).unwrap().get_size(efs).0;
        }

        for f in &self.files {
            size += f.size;
        }

        return size;
    }
}

fn main() {
    let mut input = env::current_exe().unwrap();
    input.pop();
    input.pop();
    input.pop();
    input.push("data");
    // input.push("input.txt");
    input.push("input-test.txt");

    let reader = BufReader::new(File::open(&input).expect(&format!("Cannot open {}", input.display())));
    let lines : Vec<String> = reader.lines().map(|l| l.expect("Could not parse line")).collect();

    let mut efs: HashMap<String, ElvenDirectory> = HashMap::new();
    efs.insert("/".to_string(), ElvenDirectory::new("/".to_string(), None));
    let mut current_dir_name = "/".to_string();


    for line in &lines {
        if line.starts_with("$ cd /") { continue; }
        
        if line.starts_with("$ cd ") {
            let dir = line.split_whitespace().last().unwrap().to_string();
           
            let current_dir = efs.get(&current_dir_name.clone()).unwrap();
            if dir == ".." {
                let parent = current_dir.parent.clone().unwrap();
                current_dir_name = parent;
            } else {
                let new_dir = efs.get(&dir.clone());

                if new_dir.is_none() {
                    panic!("New dir {} doesnt exist at all", dir);
                }

                if !current_dir.directories.contains(&dir.clone()) {
                    panic!("New dir {} is not a child of current dir {}", dir, current_dir_name);
                }
            }
        } else if !line.starts_with("$") {
            let mut split = line.split_whitespace();
            let first_part = split.next().unwrap();
            let name: String = split.next().unwrap().to_string();

            if first_part == "dir" {
                let new_dir = ElvenDirectory::new(name.clone(), Some(current_dir_name.clone()));
                efs.insert(name.clone(), new_dir);

                let mut current_dir = efs.get(&current_dir_name.clone()).unwrap().clone();
                current_dir.directories.push(name.clone());
                efs.insert(current_dir_name.clone(), current_dir);
            } else {
                let size: u64 = first_part.parse().unwrap();
                let new_file = ElvenFile::new(name.clone(), size);
                let mut current_dir = efs.get(&current_dir_name.clone()).unwrap().clone();
                current_dir.files.push(new_file);
                efs.insert(current_dir_name.clone(), current_dir);
            }
        }

        println!("{}", "");
    }
}
