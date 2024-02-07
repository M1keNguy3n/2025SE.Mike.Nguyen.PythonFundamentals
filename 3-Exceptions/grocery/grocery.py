hist = {}
prompt = True
while prompt:
    try:
        item = input().upper()
        if item not in hist:
            hist[item] = 1
        else:
            hist[item] += 1
    except EOFError:
        prompt = False
for i, j in hist.items():
    print(f"{j} {i}")
