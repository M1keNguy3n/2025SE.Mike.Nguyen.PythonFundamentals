import random


def main():
    level = get_level()
    count = 0
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        try: 
            ans = int(input(f"{x} + {y} = "))
        except ValueError:
        while count < 3:
            if ans != x + y:
                ans = int(input(f"{x} + {y} = "))
                count += 1
                print("EEE")

            else:
                score += 1
                break

        if count == 3:
            print(f"{x} + {y} = {x + y}")


def get_level():
    while True:
        try:
            digit = int(input("Enter a level: "))
            if digit < 4 and digit > 0:
                return digit
        except ValueError:
            continue


def generate_integer(level):
    numbers = []
    if level == 1:
        for i in range(2):
            numbers.append(random.randint(0, 9))
    if level == 2:
        for i in range(2):
            numbers.append(random.randint(10, 99))
    if level == 3:
        for i in range(2):
            numbers.append(random.randint(100, 999))
    return numbers


if __name__ == "__main__":
    main()
