import csv
import sys


def main():
    if len(sys.argv) > 4:
        sys.exit("Too few/many command-line arguments")
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    if valid(filename1) and valid(filename2):
        fix(filename1, filename2)
    else:
        sys.exit("File does not exist")


def valid(filename):
    return filename[-4::] == ".csv"


def fix(filename1, filename2):
    with open(filename1, "r") as origin:
        origin = csv.DictReader(origin)
        with open(filename2, "a") as target:
            target = csv.DictWriter(
                target, fieldnames=["first_names", "last_names", "house"]
            )
            target.writeheader()
        for row in origin:
            with open(filename2, "a") as target:
                target = csv.DictWriter(
                    target, fieldnames=["first_names", "last_names", "house"]
                )
                target.writerow(
                    {
                        "first_names": row["name"].split(",")[0].strip(),
                        "last_names": row["name"].split(",")[1].strip(),
                        "house": row["house"],
                    }
                )


if __name__ == "__main__":
    main()
