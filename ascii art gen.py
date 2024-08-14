from pyfiglet import Figlet
import sys
import random
def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        random_font= random.choice(fonts)
        figlet.setFont(font=random_font)
        s= input("Input:")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                figlet.setFont(font= sys.argv[2])
                s= input("Input:")
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

    print(figlet.renderText(s))


main()
