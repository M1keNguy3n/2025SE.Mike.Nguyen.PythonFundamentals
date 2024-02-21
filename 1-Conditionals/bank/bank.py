def main():
    str = input("").replace(" ", "").lower()


def value(str):
    if str.startswith("h") and "hello" in str:
        return "$0"
    elif str.startswith("h") and "hello" not in str:
        return "$20"
    else:
        return "$100"
