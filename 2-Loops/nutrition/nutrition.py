dict = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew": 50,
    "Kiwi": 90,
    "Lemon": 15,
    "Lime": 20,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cheries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}
fruit = input("")
try:
    print("Calories: ", dict[fruit])
except KeyError:
    print("Food not found.")
