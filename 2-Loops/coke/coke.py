sum = 0
while sum < 50:
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 20 or coin == 25 or coin == 50:
        sum += coin
    else:
        print(f"Amount due: {sum}")
        continue
    if sum < 50:
        print(f"Amount due: {sum}")
    else:
        print(f"Change owed: {sum-50}")
        break
