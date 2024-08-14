from pyfiglet import Figlet
import sys
import random
def main():
    s= input("Input:")
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 0:
        random_font= random.choice(fonts)
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 2:
        figlet.setfont(font= sys.argv[2])

    print(figlet.renderText(s))