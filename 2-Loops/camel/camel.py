str = input("")
for i in str:
    if i.isupper():
        snake = str.replace(i, f"_{i.lower()}")
try:
    print(snake)
except NameError:
    print(str)
