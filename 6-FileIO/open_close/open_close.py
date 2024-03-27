filepath = "my_text.txt"
filepath_new = "my_text1.txt"
with open(filepath, "r") as txt:
    num = txt.read()
with open(filepath, "w") as txt:
    txt.write(str(int(num) + 1))
