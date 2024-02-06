str = input("").replace(" ", "").lower()
if str.startswith("h") and str == "hello":
    print("$0")
elif str.startswith("h") and str != "hello":
    print("$20")
else:
    print("$100")
