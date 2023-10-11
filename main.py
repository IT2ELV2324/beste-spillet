#################
### MAIN FILE ###
#################
from curses import wrapper
import combat
import player
import enemies  # Vet ikke om jeg trenger denne
import items


def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr("test")

    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    wrapper(main)
