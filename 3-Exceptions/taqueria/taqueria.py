prompt = True
dict = {
    "Baja taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super burrito": 8.50,
    "Super quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla salad": 8.00,
}
item = []
sum = 0
while prompt:
    try:
        sum += dict[input().capitalize()]
        out = format(sum, ".2f")
        print(f"Total: {out}$")
    except EOFError:
        prompt = False
