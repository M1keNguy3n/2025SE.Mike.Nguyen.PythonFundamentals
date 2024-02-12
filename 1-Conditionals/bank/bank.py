str = input("").replace(" ", "").lower()
if str.startswith("h") and "hello" in str:
    print("$0")
elif str.startswith("h") and "hello" not in str:
    print("$20")
else:
    print("$100")
