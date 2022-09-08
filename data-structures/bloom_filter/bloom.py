import logging
import os

DEBUG = os.environ.get("DEBUG", "0") == "1"
logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)


class Filter:
    def __init__(self, filter_size: int, hash_count: int) -> None:
        self.filter_size = filter_size
        self.hash_count = hash_count
        self.filter = [0] * filter_size

    def add(self, key: str) -> None:
        for seed in range(self.hash_count):
            result = self.hash(key, seed)
            self.filter[result] = 1

    def might_contain(self, key: str) -> bool:
        for seed in range(self.hash_count):
            result = self.hash(key, seed)
            if self.filter[result] == 0:
                return False
        return True

    def hash(self, key: str, seed: int = 0) -> int:
        hash = 0
        for i in range(len(key)):
            hash = (hash * seed) + ord(key[i])
        ret = hash % self.filter_size
        logging.debug(f"Key: {key}\tSeed: {seed}\tHash: {ret}")
        return ret


if __name__ == "__main__":
    bloom = Filter(100, 7)
    bloom.add("hello")
    bloom.add("world")
    logging.debug(
        f"Activated Filter: {[i for i, x in enumerate(bloom.filter) if x == 1]}"
    )

    assert bloom.might_contain("hello") == True
    assert bloom.might_contain("world") == True
    assert bloom.might_contain("hello world") == False
