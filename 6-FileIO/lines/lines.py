import sys


def main():
    filename = input("Enter a file name: ")
    if valid_filename(filename):
        print(count(filename))
    else:
        sys.exit("Invalid filename")


def valid_filename(filename):
    return filename[-3::] == ".py"


def count(filename):
    count = 0
    arr = []
    with open(filename, "r") as f:
        for line in f:
            if line == "\n" or line.startswith("#") or line.startswith('"'):
                continue
            else:
                arr.append(line.rstrip())
                count += 1
    return count


if __name__ == "__main__":
    main()
