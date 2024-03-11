def word_w_length(filename):
    arr = []
    with open(filename, "r") as txt:
        for word in txt.read().rstrip().replace(".", "").replace(",", "").split():
            if len(word) == 6:
                arr.append(word)
    return arr


def word_w_length_to_file(origin, target):
    with open(target, "w") as text:
        for word in word_w_length(origin):
            text.write(word + " ")
    with open(target, "r") as text_r:
        for line in text_r.readlines():
            print(line)


def main():
    filename = "text.txt"
    print(word_w_length(filename))
    word_w_length_to_file(filename, "text_5.txt")


if __name__ == "__main__":
    main()
