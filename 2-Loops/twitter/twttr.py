str = input("")
new_string = ""
for i in str:
    if i not in ["a", "i", "e", "o", "u"]:
        new_string += i
print(new_string)
