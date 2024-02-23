from bank import value


def main():
    test_bank()


def test_bank():
    assert value("oh hello") == "$100"
    assert value("screw u") == "$100"
    assert value("hi") == "$20"
