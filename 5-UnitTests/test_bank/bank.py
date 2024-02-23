def value(str):
    if str.startswith("h") and "hello" in str:
        return "$0"
    elif str.startswith("h") and "hello" not in str:
        return "$20"
    else:
        return "$100"


def main():
    str = input("Enter a greeting: ").replace(" ", "").lower()
    print(value(str))


if __name__ == "__main__":
    main()
