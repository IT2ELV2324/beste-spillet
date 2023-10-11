#   Imports the curses library to create a window environment in the terminal
import curses

#   A main function which creates a window environment in the terminal
def main(stdscr):
    #   Clears the terminal window environment
    stdscr.clear()

    stdscr.addstr(10, 10, "Hello", curses.A_REVERSE)
    #   Refreshes the screen (similar to pygame)
    stdscr.refresh()
    #   Awaits a key input
    stdscr.getkey()

#   Initialization of the curses library that executes the main function
curses.wrapper(main)