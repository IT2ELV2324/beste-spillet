#################
### MAIN FILE ###
#################
import curses
from curses import wrapper
from curses.textpad import Textbox
from UI import *
# import combat
import player
# import enemies  # Vet ikke om jeg trenger denne
# import items


def reset_screen(stdscr, vars: list):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    current_item = vars[3]

    stdscr.resize(23, 64)
    # Clear screen
    stdscr.clear()
    stdscr.border()

    stdscr.addstr(20, 0, "├────────────────────┬────────────────────┬────────────────────┤")
    stdscr.addstr(21, 1, f"{playerName}, ")
    stdscr.addstr(str(hp), RED)
    stdscr.addstr(21, 21, f"│{areaName}")
    stdscr.addstr(21, 42, f"│{current_item}")
    stdscr.addstr(22, 0, "└────────────────────┴────────────────────┴────────────────────")

    stdscr.move(19, 1)

    stdscr.refresh()


def update_ui_info(stdscr, vars: list):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    current_item = vars[3]

    stdscr.addstr(21, 1, f"{playerName}, ")
    stdscr.addstr(str(hp), RED)
    stdscr.addstr(21, 21, f"│{areaName}")
    stdscr.addstr(21, 42, f"│{current_item}")


def reset_cursor(stdscr):
    stdscr.move(19, 1)  # Moves cursor to the lower left corner of the "screen"


def create_player(stdscr):
    stdscr.addstr(18, 1, "What is your name?")
    stdscr.addstr(19, 1, "(Press any key)")
    stdscr.getkey()
    
    input_window = curses.newwin(1, 15, 19, 1)
    input_box = Textbox(input_window)
    input_box.edit()
    
    name = input_box.gather().capitalize()
    stdscr.addstr(18, 1, "                  ")
    stdscr.addstr(19, 1, "               ")
    stdscr.addstr(18, 1, f"Very well, {name}")
    stdscr.addstr(19, 1, "(Press c to exit)")
    reset_cursor(stdscr)
    
    hero = player.Hero(name, 100)
    return hero


def init_colours():
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
    init_colours()

    playerName = "?"
    hp = 100
    areaName = "?"
    current_item = "?"
    
    reset_screen(stdscr, [playerName, 0, areaName, current_item])
    stdscr.refresh()

    player = create_player(stdscr)
    
    is_running = True
    while is_running:

        # Lat som at det er kode her #

        update_ui_info(stdscr, [player.name, player.health, areaName, current_item])
        reset_cursor(stdscr)
        stdscr.refresh()
        key = stdscr.getkey()
        if key == "c":  # Bruker 'c' som exitknapp, hvis noe annet trykkes, skjer ingenting
            is_running = False


if __name__ == "__main__":
    wrapper(main)