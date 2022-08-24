from operator import neg

class Maybe:
    def __init__(self, value, failed=False):
        self.value = value
        self.failed = failed

    def __str__(self):
        return str(self.value)

    def __or__(self, other):
        if isinstance(self, Maybe):
            return self
        return self.do(other)

    def do(self, f):
        if self.failed:
            return self
        try:
            return Maybe(f(self.value))
        except:
            return Maybe(None, failed=True)


def test_maybe_pure():
    assert Maybe(1).do(lambda x: x + 1).value == Maybe(2).value
    assert Maybe(1).do(neg).value == -1
    assert Maybe(1).do(neg).do(neg).value == (Maybe(1) | neg | neg).value == 1
    assert Maybe(3).value == (1 | 2) == 3

def test_maybe_impure():
    assert Maybe(None).do(lambda x: x + 1).value == None


if __name__ == "__main__":
    print(Maybe(1) | Maybe(2)) # failure
