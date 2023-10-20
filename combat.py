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
#   Imports the random library
import random

#   A main function
def combatMain(stdscr):
    global combatWin, enemy, attacks
    #   Prepares the screen.
    stdscr.clear()
    stdscr.resize(23, 64)
    stdscr.border()
    stdscr.refresh()

    #   Creates a window.
    combatWin = curses.newwin(UI.height-1, UI.width-2, 1, 2)
    combatWin.border()

    #   Initiates color paires.
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    combatPrep()
    run = True
    while run:
        #   Does screen matenance.
        combatUIUpkeep()

        #   Writes out the player choices, and takes a number as an input.
        combatWin.addstr(10, 0, "1. Attack", curses.color_pair(1))
        combatWin.addstr(12, 0, "2. Items", curses.color_pair(1))
        inputCharacter = combatWin.getch()

        #   If the choice was to attack, this runs.
        if inputCharacter == 1:
            #   New set of choices are given.
            for i in range(attacks):
                #   Lists the choices
                combatWin.addstr(10+i, 0, f"{i+1}. {attacks[i]}")
            combatUIUpkeep()
            inputCharacter2 = combatWin.getch()
            #   This should return an error, and wouldn't work if it didn't, this is because Hero1 is only defined in the main file, and because the enemy in the player file isn't the same enemy as in the enemies file. The player file has made its own system that doesn't work with the systems used in combat and main. It uses print, and creates its own enemy instead of importing the enemies file and using an enemy defined in it. If I had been quicker with creating the combat system, then I could've given this feedback, and we could've worked on this as a group. Sadly, things didn't go ideally, and so I will just lie down and explode. If you are reading this, Gehenna is near. The moon runs blood, The sun rises black in the sky, and the children of Caine has risen once again. The last city Gehenna has erected, and Caine is to pass his judgement on the sire diablerists. Soon, the dark mother will rise to bite the dark father, and the father will bite back, deeper.
            player.hero1.attack(attacks[inputCharacter2])
            #   Bleh
                
#   A function that prepares variables that need preparing beforehand.
def combatPrep():
    #   Chooses a random enemy from the enemies file
    enemiesList = [enemies.enemy1, enemies.enemy2, enemies.enemy3, enemies.enemy4]
    enemy = enemiesList[random.randint(0, 3)]
    attacks = list(player.Hero1.attacks.keys())




    
def combatUIUpkeep():
    #   Clears the window.
    combatWin.clear()

    #   Gets the text art from the "MonsterTextArt" file.
    monsterList = open("MonsterTextArt", "r").readlines()
    combatWin.addstr(f"HP: {enemy.hp}", curses.color_pair(2))
    for line in monsterList:
        combatWin.addstr(line, curses.color_pair(1))

    #   Refreshes the screen.
    combatWin.refresh()



#   Initiates everthing that needs initiating, and runs combatMain
curses.wrapper(combatMain)
    