import os
import sys
#from tkinter import *

#Summery of KJs programming style / problem solving skills https://www.reddit.com/r/Unexpected/comments/kybti8/watch_this/

Colours = ["Red", "Yellow"]
GridXSize = 4
GridYSize = 4


def checkCollumn(_collumn, _board):
    #Check if full (-1), empty (Index of lowest avalible slot)
    if _board[_collumn][len(_board[_collumn]) - 1] != 0:
        print("Error: Collumn Full!")
        return -1
    for i in range(0, len(_board[_collumn])):
        if _board[_collumn][i] == 0:
            return i


def updateBoard(_board, _collumn, _row, _value):
    tempBoard = []
    ix = 0
    iy = 0
    for x in _board:
        iy = 0
        if ix == _collumn:
            tempBoard.append([])
            for y in _board[_collumn]:
                if iy == _row:
                    tempBoard[_collumn].append(_value)
                else:
                    tempBoard[_collumn].append(_board[_collumn][iy])
                iy += 1
        else:
            tempBoard.append(x)
        ix += 1
    return tempBoard


def printBoard(_board, _gridXSize, _gridYSize):
    os.system("clear")
    temp2 = []
    #Flip the Array upside down, so index
    for x in range((_gridYSize - 1), -1, -1):
        temp = []
        for y in range(0, _gridXSize):
            temp.append(_board[y][x])
        temp2.append(temp)
    for i in temp2:
        print(i)
    #DisplayInTk(temp2)


def Menu():
    print("""
  _________                                     __       _____  
\_   ___ \  ____   ____   ____   ____   _____/  |_    /  |  | 
/    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\  /   |  |_
\     \___(  <_> )   |  \   |  \  ___/\  \___|  |   /    ^   /
 \______  /\____/|___|  /___|  /\___  >\___  >__|   \____   | 
        \/            \/     \/     \/     \/            |__|
  """)
    print("1. Start Game")
    print("2. Settings")
    print("3. Credits")
    print("4. Exit Game")
    Choice = input("/: ")
    if Choice == "1":
        OnAwake()
    elif Choice == "2":
        Settings()
    elif Choice == "3":
        Credits()
    elif Choice() == "4":
        sys.exit("Thanks for looking at our code?...Sure")
    else:
        print("Invalid Syntax")
        print("Returning...")
        Menu()


def Settings():
    print("Settings")
    print("Colour Combo = ", Colours[0] + Colours[1])
    print("Grid Size = ", str(GridXSize) + "" + str(GridYSize))
    print("Return to menu (type in menu)")
    Change = input("What would you like to change?: ")
    if Change.lower() in ("colour", "colour combo"):
        Colour1 = input("Colour 1: ")
        Colour2 = input("Colour 2: ")
        Colours[0] = Colour1
        Colours[1] = Colour2
        print("Returning")
        Settings()
    elif Change.lower() in ("menu", "back to menu", "return to menu","menu please"):
        Menu()
    elif Change.lower() in ("grid size", "grid system", "grid"):
        return
        #KJ do


def Credits():
    print(
        "Seb's and KJ's connect 4 except seb did the most but nvm; Haha, tbf you said not to work on it without you, but you were on yesterday...hahaha...yeah about that i was just you know bored so you know...haaahhaha..."
    )
    print("anyways hope you enjoyed our amazing game")
    print("Returning to menu")
    Menu()


def OnAwake():
    #Mini menu system
    gridXSize = int(input("Please Enter A Grid Size For the X: "))
    gridYSize = int(input("Please Enter A Grid Size For the Y: "))

    if ((gridXSize < 4) & (gridYSize < 4)):
        print("Error: Game Unwinnable!")
        Menu()
    print("")

    #This whole section looks so dumb... I love it!
    Board = [[0] * gridYSize for i in range(gridXSize)]
    #Sometimes my genious is... Its almost frightening
    print("Player 1 pick your colour out of", Colours[0] + " or " + Colours[1])
    sometimesKJsGeniousIsFrightening = input(": ")
    if sometimesKJsGeniousIsFrightening.lower() == Colours[0].lower(
    ):  #My Genious is immesurable
        WhoIsThisGuyIDidntSeeHisAttackComing = Colours[1]
    elif sometimesKJsGeniousIsFrightening.lower() == Colours[1]:
        WhoIsThisGuyIDidntSeeHisAttackComing = Colours[0]
    else:
        print("Invalid Syntax so colour", Colours[0],
              " is assigned to Player 1")
        WhoIsThisGuyIDidntSeeHisAttackComing = Colours[1]
    print("Player 2 is colour", WhoIsThisGuyIDidntSeeHisAttackComing)

    print("Starting...")
    Turn(Board, gridXSize, gridYSize)


def Turn(Board, gridXSize, gridYSize):
  #Player 1 turn
  MoveComplete = False
  while MoveComplete == False:
    #try:
      #Select Collumn
      Player1MoveC = int(
          input("P1 What column would you like to drop your counter: "))
      RowMove = checkCollumn(Player1MoveC, Board)
      #Check Collumn
      if RowMove == -1:  #Slightly more efficent, also removes the double collumn full
          MoveComplete = False
      else:
        #Update the GameBoard
        print("Move successful")
        Board = updateBoard(Board, Player1MoveC, RowMove, "X")
        printBoard(Board, gridXSize, gridYSize)
        MoveComplete = True
  #except:
  #print("Invalid Syntax")

  CheckForWin(Board)

  #Player2 Turn
  Move2Complete = False
  while Move2Complete == False:
      #try:
      Player2MoveC = int(
        input("P2 What column would you like to drop your counter: "))
      RowMove = checkCollumn(Player2MoveC, Board)
      if RowMove == -1:
        Move2Complete = False
      else:
        print("Move successful")
        Board = updateBoard(Board, Player2MoveC, RowMove, "O")
        printBoard(Board, gridXSize, gridYSize)
        Move2Complete = True
  #except:
      #print("Invalid Syntax")

  CheckForWin(Board)
  Turn(Board, gridXSize, gridYSize)


def RestartGame():
    #Asks for continuation or ends
    Choice = input("Would you like to restart the Game?: ")
    if Choice.lower() in ("y", "yes", "yeah", "yep", "why not"):
        OnAwake()
    else:
        print("Credits to Seb and KJ")
        sys.exit("Thanks for playing")


def CheckForWin(Board):
    #Checks for win for each player
    for i in range(0, 4):
        j = 0
        if Board[i][j] == Board[i][j + 1] == Board[i][j + 2] == Board[i][
                j + 3] == "X":
            print("Player 1 wins")
            print("")
            RestartGame()
        elif Board[i][j] == Board[i][j + 1] == Board[i][j + 2] == Board[i][
                j + 3] == "O":
            print("Player 2 wins")
            print("")
            RestartGame()
        elif Board[j][i] == Board[j + 1][i] == Board[j + 2][i] == Board[
                j + 3][i] == "X":
            print("Player 1 wins")
            print("")
            RestartGame()
        elif Board[j][i] == Board[j + 1][i] == Board[j + 2][i] == Board[
                j + 3][i] == "O":
            print("Player 2 wins")
            print("")
            RestartGame()


#def DisplayInTk(temp2):
#root = Tk()
#root.mainloop()
#Buttons = []
#for i in range(0, 4):
#for j in range(0, 4):
#Button = Button(root, text = temp2[i][j])
#Buttons[i].append(Button)
#Buttons[i][j].grid(row = j, column =i)
#return

Menu()
