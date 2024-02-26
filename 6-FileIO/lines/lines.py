import sys


def main():
    if len(sys.argv) >= 3:
        sys.exit("too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    filename = sys.argv[1]
    if valid_filename(filename):
        print(count(filename))
    else:
        sys.exit("Invalid filename")


def valid_filename(filename):
    return filename[-3::] == ".py"


def count(filename):
    count = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                print(line)
                if line.startswith("#") or line.startswith('"""') or line.isspace():
                    print(line)
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        return "File does not exist"
    return count


if __name__ == "__main__":
    main()
