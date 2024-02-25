def convert(fraction):
    try:
        x, y = [int(x) for x in fraction.split("/")]
        x / y
        if x > y:
            return "Invalid fraction"
    except (ZeroDivisionError, ValueError):
        return "Invalid fraction"
    return (x, y)


def gauge(x, y):
    if x / y < 0.01:
        return "E"
    elif x / y > 0.99 and x / y <= 1:
        return "F"
    else:
        ratio = format(x / y * 100, ".0f")
        return f"{ratio}%"


def main():
    fraction = input("Enter a fraction: ")
    x = convert(fraction)
    if isinstance(x, tuple):
        a, b = x
        print(gauge(a, b))
    else:
        print(x)


if __name__ == "__main__":
    main()
