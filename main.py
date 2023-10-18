#################
### MAIN FILE ###
#################
import curses
from curses import wrapper
from UI import *
# import combat
import player
# import enemies  # Vet ikke om jeg trenger denne
# import items


def reset_screen(stdscr, vars: list):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    message = vars[3]

    stdscr.resize(23, 64)
    # Clear screen
    stdscr.clear()
    stdscr.border()


    stdscr.addstr(20, 0, "├────────────────────┬────────────────────┬────────────────────┤")
    stdscr.addstr(21, 1, f"     {playerName}, ")
    stdscr.addstr(str(hp), RED)
    stdscr.addstr(21, 21, f"│     {areaName}")
    stdscr.addstr(21, 42, f"│      {message}")
    stdscr.addstr(22, 0, "└────────────────────┴────────────────────┴────────────────────")

    stdscr.move(19, 1)

    stdscr.refresh()


def update_ui_info(stdscr, vars: list):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    message = vars[3]

    stdscr.addstr(21, 1, f"     {playerName}, ")
    stdscr.addstr(str(hp), RED)
    stdscr.addstr(21, 21, f"│     {areaName}")
    stdscr.addstr(21, 42, f"│      {message}")


def reset_cursor(stdscr):
    stdscr.move(19, 1)  # Moves cursor to the lower left corner of the "screen"


def create_player(stdscr):
    pass


def init_all_colours():
    # RED
    global RED, GREEN, YELLOW, BLUE, ORANGE, PURPLE
    curses.init_pair(1, curses.COLOR_RED, -1)
    RED = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    GREEN = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    YELLOW = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    BLUE = curses.color_pair(4)


def main(stdscr):

    curses.use_default_colors()
    init_all_colours()

    playerName = "Kjell"
    hp = 100
    areaName = "Området"
    message = "test"
    
    reset_screen(stdscr, [playerName, hp, areaName, message])
    stdscr.refresh()
    
    is_running = True
    while is_running:

        # Lat som at det er kode her #

        update_ui_info(stdscr, [playerName, hp, areaName, message])
        reset_cursor(stdscr)
        stdscr.refresh()
        key = stdscr.getkey()
        if key == "c":  # Bruker 'c' som exitknapp, hvis noe annet trykkes, skjer ingenting
            is_running = False


if __name__ == "__main__":
    wrapper(main)