#! /usr/bin/env python
# simple trie implementation using dict


NULL = object()


class Trie(dict):
    def add(self, word):
        node = self
        _len = len(word)

        for i, letter in enumerate(word, 1):
            if letter in node:
                next_node = node[letter]
            else:
                next_node = Trie()
            if i == _len:
                next_node[None] = NULL
            node[letter] = next_node
            node = next_node

    def search(self, word):
        node = self
        _len = len(word)

        for i, letter in enumerate(word, 1):
            if letter in node:
                node = node[letter]
            else:
                return False
            if i == _len and None in node:
                return node
