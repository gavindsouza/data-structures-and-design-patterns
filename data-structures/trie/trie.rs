use std::collections::HashMap;

// struct Trie(HashMap<char, Trie>);

trait Trie {
    fn add(&mut self, word: &str);
    fn search(&self, word: &str) -> bool;
    fn like(&self, word: &str) -> bool;
    fn generate_words(&self, prefix: &str) -> Vec<String>;
}

impl Trie for HashMap<String, HashMap> {
    pub fn add(&mut self, word: &str) {
        let mut node = self;
        let mut next_node: HashMap;
        let _len = word.len();

        for (i, letter) in word.chars().enumerate() {
            println!("{} {}", i, letter);
            // if node.contains_key(&letter) {
            //     next_node = node.get(&letter).unwrap();
            // } else {
            //     next_node = Trie::new();
            // }
            //     node.0.get_mut(&letter).unwrap().add(&word[i + 1..]);
            // } else {
            //     node.0.insert(letter, Trie::new());
            //     node.0.get_mut(&letter).unwrap().add(&word[i + 1..]);
            // }
        }
    }

    pub fn search(&self, word: &str) -> bool {
        false
    }

    pub fn like(&self, word: &str) -> bool {
        false
    }

    // pub fn generate_words(&self, prefix: &str, node: Trie) -> Vec<String> {

    // }
}

fn main() {
    let mut trie = new HashMap<String, HashMap>();
    trie.add("hello");
    println!("Now lets implement this trie in rust!");
}