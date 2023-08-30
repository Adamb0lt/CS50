from pyfiglet import Figlet
figlet=Figlet()
import sys
#may need to import requests
import random # need this to select a random font from the list of fonts

def main():
    if len(sys.argv) == 3:
        two()
    elif len(sys.argv) == 1:
        zero()
    else:
        sys.exit("Invalid Usage")



def two():
    #while loop to ask check for formatting and also font
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in figlet.getFonts(): # .getFonts should have the list of fonts
            f = figlet.setFont(font = sys.argv[2])
            p = input("Input: ").split("-")
            print("Output:\n",figlet.renderText(p[0]))
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")



def zero():
    # takes input, chooses a random font from the getFonts and then applies it to the text
    t = input("Input: ")
    g = random.choice(figlet.getFonts())
    s = figlet.setFont(font = g)
    print("Output:\n",figlet.renderText(t))

if __name__ == "__main__":
    main()



