from fuel import convert


def test_convert():
    assert convert("5/4") == "Enter a fraction: "
    assert convert("4/5") == (4, 5)
