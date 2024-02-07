exp = input("")
x, y, z = exp.split(" ")
match y:
    case "+":
        print(float(int(x) + int(z)))
    case "-":
        print(float(int(x) - int(z)))
    case "*":
        print(float(int(x) * int(z)))
    case "/":
        print(float(int(x) / int(z)))
