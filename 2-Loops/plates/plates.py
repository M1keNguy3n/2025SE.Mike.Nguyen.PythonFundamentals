def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    digits = ""
    for i in s:
        if i.isnumeric():
            digits += i
    if digits.startswith("0"):
        return False
    if not s.isidentifier():
        return False
    return True


main()
