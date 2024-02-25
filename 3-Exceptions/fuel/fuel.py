def convert():
    prompt = True
    while prompt:
        try:
            x, y = [int(x) for x in (input("Enter a fraction: ").split("/"))]
            x / y
            if x > y:
                continue
            prompt = False
        except (ZeroDivisionError, ValueError):
            continue
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
    x, y = convert()
    print(x, y)


if __name__ == "__main__":
    main()
