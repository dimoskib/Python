from termcolor import colored
import pyfiglet
from colorama import init
init()


valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input("What would you like to print? ")
color = input("What color? ")
if color.lower() not in valid_colors:
    color = 'magenta'
# This should be a very long commentar so the autopep8 change it
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)
