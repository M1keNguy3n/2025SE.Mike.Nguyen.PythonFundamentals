from pyfiglet import Figlet
import sys

figlet = Figlet()
arg1 = sys.argv[1]
arg2 = sys.argv[2]
if arg1 != "-f" and arg1 != "--font":
    sys.exit("Error")
if arg2 not in figlet.getFonts() or arg2 not in figlet.getFonts():
    sys.exit("Not a font")
text = input("")
figlet.setFont(font=arg2)
print(figlet.renderText(text))
