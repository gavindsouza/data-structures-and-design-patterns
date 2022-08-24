## Stuff that I do to scratch an itch

Implemented a trie in Python because I've been obsessed with it since I learnt about it first a few years ago. I'll be adding more stuff that I "feel" like trying or if I have any newer, better ideas.

Been learning Rust because it's so cool. Started implementing Trie in Rust and wanted to benchmark while integrating it as a Python module :D That's a wip until I decide to get back to it.

### Contents

1. Trie

A bare bones implementation of Trie using Dict that supports the following operations:

  - Add a word (`str`) to the Trie
  - Check if word exists in Trie
  - Generate all words in Trie from a particular node

The module consists of:
  - a Python implementation
  - a Rust equivalent _[wip]_

Benchmarks:

Size of input dictionary: 966,550 words. Size of test dictionary: 10,000 words. Numbers generated using _Python3.10.4_ on _AMD Ryzen 7 PRO_.

| Structure | Inserting dictionary | Full Search | Prefixed Search |
| - | - | - | - |
| Trie _(Dict based)_ | 2.18e+00s | 1.19e-02s | 9.88e+00s |
| Set | 1.11e-01s | 8.28e-04s | 1.26e-03s |
| List | 2.34e-02s | 4.99+01s | 6.61e+02s |

> The `suggestions.py` script provides a use case for Trie that takes string inputs and give suggestions for similar words if the word/phrase doesn't exist in the data structure.

2. Monad
