while True:
    try:
        choice = input(
            """ There's an intersection. Which way should you go?
        1. Left
        2. Right
        3. Straight
        4. Go home
    Enter your choice (1, 2, 3 or 4): """
        )
    except EOFError:
        continue
    if not choice.isnumeric():
        continue
    if choice == "4":
        print("You gave up.")
        break
