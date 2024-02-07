def convert(time: str):
    """Assumes time is a string, converts to float and return."""
    hour, minute = time.split(":")
    return float(hour) + (float(minute) / 60)


def main():
    time = input("")
    float = convert(time)
    if 7 <= float and float <= 8:
        print("breakfast time")
    elif 12 <= float and float <= 13:
        print("lunch time")
    elif 18 <= float and float <= 19:
        print("dinner time")
    else:
        print("nothing")


if __name__ == "__main__":
    main()
