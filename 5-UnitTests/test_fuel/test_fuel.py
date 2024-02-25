from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("5/4") == "Invalid fraction"
    assert convert("4/0") == "Invalid fraction"
    assert convert("4/s") == "Invalid fraction"
    assert convert("a/5") == "Invalid fraction"
    assert convert("4/5") == (4, 5)
    assert convert("0/5") == (0, 5)


def test_gauge():
    assert gauge(0, 5) == "E"
    assert gauge(0.991, 1) == "F"
    assert gauge(4, 5) == "80%"
    assert gauge(3, 5) == "60%"
