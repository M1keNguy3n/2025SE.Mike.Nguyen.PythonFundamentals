import inflect

p = inflect.engine()
arr = []
while True:
    try:
        arr.append(input())
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(arr)}")
