##############
### COMBAT ###
##############

#   Imports the curses library for use in terminal formatting.
import curses
#   Import the curses library's textpad library.
import curses.textpad
#   Imports the enemies file.
import enemies
#   Imports the player file.
import player
#   Imports the UI file.
import UI

#   A main function
def combatMain():
    run = True
    while run:
        pass
        


#   A UI function for preparation of the UI
def combatUI(stdscr):
    stdscr.clear()
    stdscr.resize(23, 64)
    stdscr.border()
    stdscr.refresh()


def combatFunc():
    #   Creates a window
    combatWin = curses.newwin(UI.height, UI.width, 1, 1)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    monsterList = open("MonsterTextArt", "r").readlines()
    for line in monsterList:
        combatWin.addstr(line, curses.color_pair(5))

    combatWin.refresh()
    combatWin.getkey()

curses.wrapper(combatUI)
    