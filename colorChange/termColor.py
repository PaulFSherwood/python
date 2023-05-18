## following from https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python
##
import sys

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def red():
    sys.stdout.write(RED)

def blue():
    sys.stdout.write(BLUE)

def cyan():
    sys.stdout.write(CYAN)

def green():
    sys.stdout.write(GREEN)

def reset():
    sys.stdout.write(RESET)

def bold():
    sys.stdout.write(BOLD)

def reverse():
    sys.stdout.write(REVERSE)

