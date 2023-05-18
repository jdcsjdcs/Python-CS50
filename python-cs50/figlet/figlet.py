from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and sys.argv[2] in figlet.getFonts()
):
    figlet.setFont(font=sys.argv[2])

elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

else:
    sys.exit("Invalid usage")

s = input("Input: ")
print(figlet.renderText(s))
