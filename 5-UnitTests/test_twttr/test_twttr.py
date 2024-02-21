from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    tests = {"watermelon": "wtrmln", "cake": "ck", "twitter": "twttr"}
    for i, j in tests.items():
        try:
            assert shorten(i) == j
        except AssertionError:
            print(f"Failed test, returned {shorten(i)}")


if __name__ == "__main__":
    main()
