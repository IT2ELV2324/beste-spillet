#################
### MAIN FILE ###
#################
import curses
from textcodes import *
from curses import wrapper
from UI import *
# import combat
# import player
# import enemies  # Vet ikke om jeg trenger denne
# import items


def init_ui(stdscr, vars):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    message = vars[3]

    stdscr.resize(22, 62)
    # Clear screen
    stdscr.clear()


    stdscr.addstr(19, 0, "├────────────────────┬───────────────────┬───────────────────┤")
    stdscr.addstr(20, 1, f"     {playerName}, ")
    stdscr.addstr(str(hp), curses.COLOR_RED)
    stdscr.addstr(20, 21, f"│     {areaName}")
    stdscr.addstr(20, 41, f"│      {message}")
    stdscr.addstr(21, 0, "└────────────────────┴───────────────────┴───────────────────")

    stdscr.move(18, 1)

    stdscr.refresh()


def update_ui_info(stdscr, vars):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    message = vars[3]

    stdscr.addstr(20, 1, f"     {playerName}, ")
    stdscr.addstr(str(hp), curses.COLOR_RED)
    stdscr.addstr(20, 21, f"│     {areaName}")
    stdscr.addstr(20, 41, f"│      {message}")


def reset_cursor(stdscr):
    stdscr.move(18, 1)

def main(stdscr):

    playerName = "Kjell"
    hp = 100
    areaName = "Området"
    message = "test"
    
    init_ui(stdscr, [playerName, hp, areaName, message])
    stdscr.refresh()
    
    is_running = True
    while is_running:

        # Lat som at det er kode her #

        update_ui_info(stdscr, [playerName, hp, areaName, message])
        reset_cursor(stdscr)
        stdscr.refresh()
        key = stdscr.getkey()
        if key == "c":
            is_running = False


if __name__ == "__main__":
    wrapper(main)
