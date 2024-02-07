prompt = True
while prompt:
    try:
        x, y = [int(x) for x in (input("Enter a fraction: ").split("/"))]
        x / y
        if x > y:
            continue
        prompt = False
    except (ZeroDivisionError, ValueError):
        continue

if x / y < 0.01:
    print("E")
elif x / y > 0.99 and x / y <= 1:
    print("F")
else:
    ratio = format(x / y * 100, ".0f")
    print(f"{ratio}%")
