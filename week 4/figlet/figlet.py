# Import library to use
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


#Bounderies of command line: 0 - 2 arguments

#0: name of the file
if len(sys.argv) == 1:
# list of the possible fonts
    fonts = figlet.getFonts()
#1 argument = random font
    random_font = random.choice(fonts)
#set the font
    figlet = Figlet(figlet.setFont(font=random_font))


#3 arguments = specific font
#1st arg = -f or --font / 2nd arg = name of the font
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet = Figlet(font=sys.argv[2])


# otherwise exit + error message
else:
    sys.exit("Invalid usage")


# Prompt user for a str
prompt = input("Input: ")


# Output the text in the desired font
print("Output: ", figlet.renderText(prompt))
