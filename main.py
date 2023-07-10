from calcs import *
from utils import stringerize
from lexer import tokenize_float
import os

mode = 'float'

while True:
    text = input(f'Enter {mode} expression (Type "quit" to exit, "help" for help): ')

    if text == 'quit':
        break
    if text == 'clear':
        os.system('clear')
    if text == 'help':
        help_text = 'Welcome to PyMath, the step-by-step calculator written in python.\nRunning PyMath puts you into a prompt where you can input mathematical expressions.\n\nHere are the commands available in the prompt:\nquit - exits the program\nhelp - runs this command\nmode - toggles between float and decimal mode'
        print(help_text)
    else:
        expression = tokenize_float(text)

        print(' ', stringerize(expression))
        
        while len(expression) > 1:
            expression = calc_float(expression)
            print('=', stringerize(expression))
