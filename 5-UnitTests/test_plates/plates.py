def main():
    plate = input("Plate: ")
    print(is_valid(plate))


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return "Invalid"
    if not s[0:2].isalpha():
        return "Invalid"
    digits = ""
    for i in s:
        if i.isnumeric():
            digits += i
    if digits.startswith("0"):
        return "Invalid"
    if not s.isidentifier():
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()
