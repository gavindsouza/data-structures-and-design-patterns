#! /usr/bin/env python3
# simple trie implementation using dict


from typing import Optional, Tuple, Union, List


NULL = object()


class Trie(dict):
    __slots__ = ()

    def add(self, word: str) -> None:
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

    def _search(self, word: str) -> Tuple[str, Union["Trie", "None"]]:
        node = self

        for letter in word:
            if letter not in node:
                return "", None
            node = node[letter]
        # if you've reached the end of the word, check
        # if None exists to mark the end of the word
        if None in node:
            return word, node
        return "", None

    def _like(self, word: str) -> Tuple[List[str], Union["Trie", "None"]]:
        node = self
        first = True
        for letter in word:
            if letter not in node and not first:
                return "", None
            first = False
            node = node[letter]
        return self.generate_words(node=node), node

    def search(self, word: str) -> bool:
        """Search for a word in the trie.

        Usage:
            >>> from trie import Trie
            >>> t = Trie()
            >>> for name in ["gavin", "gavino", "stale", "stella", "stellar"]:
            ...     t.add(name)
            ...
            >>> t.search("gavin")
            True
            >>> t.search("stale")
            False
        """
        word, node = self._search(word=word)
        return node is not None and node[None] is NULL

    def like(self, word: str) -> List[str]:
        """Generate all words in the trie that start with the given prefix.

        Usage:
            >>> from trie import Trie
            >>> t = Trie()
            >>> for name in ["gavin", "gavino", "stale", "stella", "stellar"]:
            ...     t.add(name)
            ...
            >>> t.like("gav")
            ['gavin', 'gavino']
        """
        endings, nodes = self._like(word=word)
        return [f"{word}{ending}" for ending in endings]

    def generate_words(
        self, prefix: str = "", node: Optional["Trie"] = None
    ) -> List[str]:
        """Generate all words in the trie that start with the given prefix.

        Usage:
            >>> from trie import Trie
            >>> t = Trie()
            >>> for name in ["gavin", "gavino", "stale", "stella", "stellar"]:
            ...     t.add(name)
            ...
            >>> t.generate_words(node=t['g'])
            ['avin', 'avino']
        """
        node = node or self
        words = []

        for key in node:
            if key is None:
                words.append(prefix)
            else:
                words.extend(self.generate_words(prefix + key, node[key]))
        return words
