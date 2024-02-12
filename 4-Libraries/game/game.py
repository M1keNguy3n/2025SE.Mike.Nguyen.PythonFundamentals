import random

while True:
    try:
        level = int(input("Enter a level: "))
        break
    except EOFError | ValueError:
        continue

num = random.randint(0, level)

while True:
    guess = int(input("Guess: "))
    if guess > level:
        print("Too large!")
        continue
    elif guess < 0:
        print("Too small!")
        continue
    elif guess == num:
        break
print("Just right!")
