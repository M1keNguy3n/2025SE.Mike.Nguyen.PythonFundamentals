def word_count(filename):
    with open(filename, "r") as anthem:
        count = 0
        for line in anthem:
            count += len(line.split(" "))
    return count
