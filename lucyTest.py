#   Imports the curses library to create a window environment in the terminal
import curses

#   A main function which creates a window environment in the terminal
def main(stdscr):
    #   Debug print
    print("a")
    #   Clears the terminal window environment
    stdscr.clear()
    #   Debug print
    print("a")
    #   I have no idea what thesedo
    stdscr.refresh()
    stdscr.getkey()

#   Initialization of the curses library that executes the main function
curses.wrapper(main)