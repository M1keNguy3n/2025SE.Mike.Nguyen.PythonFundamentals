import csv
import sys
from tabulate import tabulate


def tabler(filename):
    arr = []
    with open(filename, "r") as csv_file:
        menu = csv.reader(csv_file)
        for line in menu:
            arr.append(line)
        print(tabulate(arr))


def valid(filename):
    return filename[-4::] == ".csv"


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few/many command-line arguments")
    filename = sys.argv[1]
    if valid(filename):
        tabler(filename)
    else:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
