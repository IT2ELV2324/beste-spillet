##############
### COMBAT ###
##############

#   Imports the curses library for use in terminal formatting.
import curses
#   Imports the enemies file
import enemies
#   Imports the player file
import player
#   Imports the UI file
import UI

#   A main function
def combatMain():
    run = True
    while run:
        


#   A UI function for preparation of the UI
def combatUI():
    #   Creates a window
    combatWin = curses.newwin(UI.height, UI.width)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    monsterList = open("MonsterTextArt", "r").readlines()
    for line in monsterList:
        combatWin.addstr(line, curses.color_pair(1))
    