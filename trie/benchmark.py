import sys
import timeit
from contextlib import contextmanager
from random import choices, randint
from string import ascii_letters

from trie import Trie


@contextmanager
def time_this(var: str):
    start_time = timeit.default_timer()
    try:
        yield
    finally:
        elapsed = timeit.default_timer() - start_time
        print(f"{var} took {elapsed:.2e} seconds")


def generate_random_word(length: int = None) -> str:
    length = length or randint(1, 12)
    return "".join(choices(ascii_letters, k=length))


def get_size(obj, seen: set = None) -> int:
    """Recursively finds size of objects"""
    # from https://goshippo.com/blog/measure-real-size-any-python-object/

    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum(get_size(v, seen) for v in obj.values())
        size += sum(get_size(k, seen) for k in obj.keys())
    elif hasattr(obj, "__dict__"):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_size(i, seen) for i in obj)
    return size


def benchmark_trie(input_data: list[str], test_data: list[str]):
    _trie = Trie()
    _list = list()
    _set = set()

    with time_this("Adding words to trie"):
        for word in input_data:
            _trie.add(word)
    with time_this("Searching in trie"):
        for w in test_data:
            _trie.search(w)
    with time_this("Prefixed search in trie"):
        for w in test_data:
            _trie.like(w)
    print(f"Size of trie: {get_size(_trie) // (1024 ** 2):,} MB\n")

    with time_this("Adding words to set"):
        for word in input_data:
            _set.add(word)
    with time_this("Searching in set"):
        for w in test_data:
            w in _set
    with time_this("Prefixed search in set"):
        for w in test_data:
            {x for x in _list if x.startswith(w)}
    print(f"Size of set: {get_size(_set) // (1024 ** 2):,} MB\n")

    with time_this("Adding words to list"):
        for word in input_data:
            _list.append(word)
    with time_this("Searching in list"):
        for w in test_data:
            w in _list
    with time_this("Prefixed search in list"):
        for w in test_data:
            [x for x in _list if x.startswith(w)]
    print(f"Size of list: {get_size(_list) // (1024 ** 2):,} MB\n")


if __name__ == "__main__":
    words = [generate_random_word() for _ in range(500_000)]
    non_existent_words = [generate_random_word() for _ in range(5_000)]
    find_words = choices(words, k=5_000) + non_existent_words

    print(f"Size of input dictionary: {len(words):,} words")
    print(f"Size of test dictionary: {len(find_words):,} words")
    print()

    benchmark_trie(input_data=words, test_data=find_words)
