#################
### MAIN FILE ###
#################
import curses
from curses import wrapper
from curses.textpad import Textbox
from UI import *
import combat_temp
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
    stdscr.addstr(21, 1, center_text(f"{playerName}, {str(hp)}"))
    stdscr.addstr(playerName + ", ")
    stdscr.addstr(str(hp), RED)
    stdscr.addstr(21, 21, f"│{center_text(areaName)}")
    stdscr.addstr(areaName)
    stdscr.addstr(21, 42, f"│{center_text(current_item)}")
    stdscr.addstr(current_item)
    stdscr.addstr(22, 0, "└────────────────────┴────────────────────┴────────────────────")

    stdscr.move(19, 1)

    stdscr.refresh()


def update_ui_info(stdscr, vars: list):

    playerName = vars[0]
    hp = vars[1]
    areaName = vars[2]
    current_item = vars[3]

    stdscr.addstr(21, 1, center_text(f"{playerName}, {str(hp)}"))
    stdscr.addstr(f"{playerName}, ")
    stdscr.addstr(str(hp), RED)
    stdscr.addstr(21, 21, f"│{center_text(areaName)}")
    stdscr.addstr(areaName)
    stdscr.addstr(21, 42, f"│{center_text(current_item)}")
    stdscr.addstr(current_item)


def reset_cursor(stdscr):
    stdscr.move(19, 1)  # Moves cursor to the lower left corner of the "screen"


def create_player(stdscr):
    stdscr.addstr(18, 1, "What is your name?")
    stdscr.addstr(19, 1, "(Press any key)", curses.A_ITALIC | curses.A_BOLD)
    stdscr.getkey()
    
    input_window = curses.newwin(1, 15, 19, 1)
    input_box = Textbox(input_window)
    input_box.edit()
    
    name = input_box.gather().capitalize()
    stdscr.addstr(18, 1, "                  ")
    stdscr.addstr(19, 1, "               ")
    if name[:6] != "Harald":
        stdscr.addstr(17, 1, "Are you alright? Your name is Harald Helt! Seems you got")
        stdscr.addstr(18, 1, "quite messed up by that guy Slemsing")
    else:
        stdscr.addstr(18, 1, "That's good, Harald. Seems you're not as knocked as we feared")
    stdscr.addstr(19, 1, "(Press c to exit)", curses.A_REVERSE)
    reset_cursor(stdscr)
    
    hero = player.Hero("Harald Helt", 100)
    return hero


def init_colours():
    # All Colour pairs needed
    global RED, GREEN, YELLOW, BLUE
    curses.init_pair(1, curses.COLOR_RED, -1)
    RED = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    GREEN = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    YELLOW = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    BLUE = curses.color_pair(4)


def center_text(text):
    return " " * ((20 - len(text)) // 2)


def move_cursor(stdscr, dir):
    match dir:
        case curses.KEY_LEFT:
            stdscr.move(0, 1)
        case curses.KEY_RIGHT:
            pass
        case curses.KEY_UP:
            pass
        case curses.KEY_DOWN:
            pass


def main(stdscr):

    curses.use_default_colors()
    init_colours()

    movement_keys = [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN]
    areaName = "?"
    current_item = "?"
    
    reset_screen(stdscr, ["?", 0, areaName, current_item])
    stdscr.refresh()

    player = create_player(stdscr)
    reset_cursor(stdscr)
    
    is_running = True
    while is_running:

        # Lat som at det er kode her #
        update_ui_info(stdscr, [player.name, player.health, areaName, current_item])

        stdscr.refresh()
        key = stdscr.getkey()
        if key in movement_keys:
            move_cursor(stdscr, key)
        if key == 'c' or key == 'C':  # Bruker 'c' som exitknapp, hvis noe annet trykkes, skjer ingenting
            is_running = False
        if key == 'f' or key == 'F':
            combat_temp.combatFunc()
        if key == 'r' or key == 'R':
            reset_cursor()


if __name__ == "__main__":
    wrapper(main)