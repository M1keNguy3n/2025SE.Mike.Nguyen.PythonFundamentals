def main():
    str = input("")
    print(shorten(str))


def shorten(str):
    new_string = ""
    for i in str:
        if i not in ["a", "i", "e", "o", "u"]:
            new_string += i
    return new_string


if __name__ == "__main__":
    main()
