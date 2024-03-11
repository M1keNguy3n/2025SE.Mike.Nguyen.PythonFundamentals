from word_count import word_count


def test_count():
    filename = "anthem.txt"
    assert word_count(filename) == 108
