from plates import is_valid


def main():
    test_valid()
    test_invalid()


def test_valid():
    assert is_valid("CS50") == "Valid"


def test_invalid():
    assert is_valid("CS05") == "Invalid"
    assert is_valid("CS50P") == "Invalid"
    assert is_valid("PI3.14") == "Invalid"
    assert is_valid("H") == "Invalid"
    assert is_valid("OUTATIME") == "nvalid"


if __name__ == "__main__":
    main()
