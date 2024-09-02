import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    get_input = input('Input: ')
    print(figlet.renderText(get_input))
elif sys.argv[1] == '-f' and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    get_input = input('Input: ')
    print(figlet.renderText(get_input))
else:
    sys.exit('Invalid usage')
    
