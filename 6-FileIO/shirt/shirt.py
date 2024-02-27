import os.path
import sys
from PIL import Image as im
from PIL import ImageOps as io


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    filepath1 = sys.argv[1]
    filepath2 = sys.argv[2]
    print(filepath1, filepath2)
    valid(filepath1, filepath2)
    try:
        input = im.open(filepath1)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = im.open("shirt.png")
    input = io.fit(image=input, size=shirt.size)
    input.paste(shirt, shirt)
    input.save(filepath2)


def valid(filepath1, filepath2):
    extensions = [".jpg", ".png", ".jpeg"]
    input_extension = os.path.splitext(filepath1)[1].lower()
    output_extension = os.path.splitext(filepath2)[1].lower()
    if input_extension not in extensions:
        sys.exit("Invalid input.")
    if output_extension not in extensions:
        sys.exit("Invalid input.")
    if input_extension != output_extension:
        sys.exit("Different extensions.")


if __name__ == "__main__":
    main()
