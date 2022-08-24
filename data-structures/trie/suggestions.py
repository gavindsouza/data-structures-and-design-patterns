from trie import Trie


if __name__ == "__main__":
    # TODO: Take live inputs and give word suggestions using trie
    with open("../clojure-spellchecker/resources/words.txt") as f:
        words = f.read().splitlines()
    trie = Trie()
    for word in words:
        trie.add(word)
    del words

    while True:
        word = input("Enter a word: ")
        if trie.search(word):
            print("Word is in dictionary")
        print(f"Suggestions: {trie.like(word)}")
