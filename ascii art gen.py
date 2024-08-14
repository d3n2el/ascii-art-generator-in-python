from pyfiglet import Figlet
import sys
import random
def main():
    s= input("Input:")
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        random_font= random.choice(fonts)
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                figlet.setFont(font= sys.argv[2])
            else:
                print("Invalid Font")

    print(figlet.renderText(s))


main()
