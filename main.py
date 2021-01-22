import os
import sys

#from tkinter import *

#Summery of KJs programming style / problem solving skills https://www.reddit.com/r/Unexpected/comments/kybti8/watch_this/

Colours = ["Red", "Yellow"]
gridXSize = 4
gridYSize = 4


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


def Menu(gridXSize, gridYSize):
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
      Board = [[0] * gridYSize for i in range(gridXSize)]
      OnAwake(Board, gridXSize, gridYSize)
  elif Choice == "2":
      Settings(gridXSize, gridYSize)
  elif Choice == "3":
      Credits()
  elif Choice() == "4":
      sys.exit("Thanks for looking at our code?...Sure")
  else:
      print("Invalid Syntax")
      print("Returning...")
      Menu(gridXSize, gridYSize)


def Settings(gridXSize, gridYSize):
  print("Settings")
  print("Colour Combo = ", Colours[0] + " " + Colours[1])
  print("Grid Size = ", str(gridXSize) + " " + str(gridYSize))
  print("#Note changing grid size will cause the game to begin")
  print("Return to menu (type in menu)")
  Change = input("What would you like to change?: ")
  if Change.lower() in ("colour", "colour combo"):
      Colour1 = input("Colour 1: ")
      Colour2 = input("Colour 2: ")
      Colours[0] = Colour1
      Colours[1] = Colour2
      print("Returning")
      Settings()
  elif Change.lower() in ("menu", "back to menu", "return to menu",
                          "menu please"):
      Menu(gridXSize, gridYSize)
  elif Change.lower() in ("grid size", "grid system", "grid"):
      Incorrect = True
      while Incorrect:
          gridXSize = int(input("Please Enter A Grid Size For the X: "))
          gridYSize = int(input("Please Enter A Grid Size For the Y: "))
          if ((gridXSize < 4) & (gridYSize < 4)):
              print("Error: Game Unwinnable!")
              print("Try again")

          else:
              Incorrect = True
              Board = [[0] * gridYSize for i in range(gridXSize)]
              OnAwake(Board, gridXSize, gridYSize)
  else:
      print("Invalid Syntax")
      Settings(gridXSize, gridYSize)


def Credits():
  print(
      "Seb's and KJ's connect 4 except seb did the most but nvm; Haha, tbf you said not to work on it without you, but you were on yesterday...hahaha...yeah about that i was just you know bored so you know...haaahhaha..."
  )
  print("anyways hope you enjoyed our amazing game")
  print("Returning to menu")
  Menu(gridXSize, gridYSize)


def OnAwake(Board, gridXSize, gridYSize):
  #This whole section looks so dumb... I love it!
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
      try:
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
      except:
          print("Invalid Syntax")

  CheckForWin(Board, gridXSize, gridYSize)

  #Player2 Turn
  Move2Complete = False
  while Move2Complete == False:
      try:
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
      except:
          print("Invalid Syntax")

  CheckForWin(Board, gridXSize, gridYSize)
  Turn(Board, gridXSize, gridYSize)


def RestartGame(gridXSize, gridYSize):
  #Asks for continuation or ends
  Choice = input("Would you like to restart the Game?: ")
  if Choice.lower() in ("y", "yes", "yeah", "yep", "why not"):
      Menu(gridXSize, gridYSize)
  else:
      print("Credits to Seb and KJ")
      sys.exit("Thanks for playing")


def CheckForWin(Board, gridXSize, gridYSize):
  CheckHorizontal(Board, gridXSize, gridYSize)
  CheckVertical(Board, gridXSize, gridYSize)
  CheckDiagonal(Board, gridXSize, gridYSize)


def CheckHorizontal(Board, gridXSize, gridSsize):
  Count = 0
  CountP2 = 0
  for y in range(0, gridYSize):
    for x in range (0, gridXSize):
      if Board[x][y] == "X"  :
        Count += 1
        if Count == 4:
          print("Player 1 Wins")
          RestartGame(gridXSize, gridYSize)
      else:
        Count = 0
        
      if Board[x][y] == "O":
        CountP2 += 1
        if CountP2 == 4:
          print("Player 2 Wins")
          RestartGame(gridXSize, gridYSize)
      else:
        CountP2 = 0

def CheckVertical(Board, gridXSize, gridYSize):
  Count = 0
  CountP2 = 0
  for x in range(0, gridXSize):
    for y in range(0, gridYSize):
      if Board[x][y] == "X":
        Count += 1
        if Count == 4:
          print("Player 1 Wins")
          RestartGame(gridXSize, gridYSize)
      else:
        Count = 0

      if Board[x][y] == "O":
        CountP2 += 1
        if CountP2 == 4:
          print("Player 2 Wins")
          RestartGame(gridXSize, gridYSize)
      else:
        CountP2 = 0 

def CheckDiagonal(Board, gridXSize, gridYSize):
  for x in range(0, gridXSize):
    y = 0
    CheckDiagonalR(Board, gridXSize, gridYSize, x, y)
    CheckDiagonalL(Board, gridXSize, gridYSize, x, y)
  for y in range(0, gridYSize):
    x = 0
    CheckDiagonalR(Board, gridXSize, gridYSize, x, y)
    x = gridXSize - 1
    CheckDiagonalL(Board, gridXSize, gridYSize, x, y)


def CheckDiagonalL(Board, gridXSize, gridYSize, x, y):
  Count = 1 if Board[x][y] == "X" else 0
  CountP2 = 1 if Board[x][y] == "O" else 0
  while ((y + 1) < (gridYSize)) & ((x - 1) < gridXSize):
      x -= 1
      y += 1
      Count = Count + 1 if Board[x][y] == "X" else 0 
      CountP2 = CountP2 + 1 if Board[x][y] == "X" else 0 
      if Count == 4:
        print("Player 1 Wins")
        RestartGame(gridXSize, gridYSize)
      if CountP2 == 4:
        print("Player 2 Wins")
        RestartGame(gridXSize, gridYSize) 
  


def CheckDiagonalR(Board, gridXSize, gridYSize, x, y):
  Count = 1 if Board[x][y] == "X" else 0
  CountP2 = 1 if Board[x][y] == "O" else 0
  while ((x + 1) < gridXSize) & ((y + 1) < gridYSize):
    x += 1
    y += 1
    Count = Count + 1 if Board[x][y] == "X" else 0
    CountP2 = CountP2 + 1 if Board[x][y] == "O" else 0
    if Count == 4:
      print("Plyer 1 Wins")
      RestartGame(gridXSize, gridYSize)
    if CountP2 == 4:
      print("Player 2 Wins")
      RestartGame(gridXSize, gridYSize)    



  #DILIGAF How ugly and inefficient this is going to be, refere to :
  #https://www.reddit.com/r/Unexpected/comments/kybti8/watch_this/
  #For an explaination

  

  
  # y = 0
  # for k in range(0, gridYSize):
  #   while k <= gridYSize:
  #     for x in range(0, gridXSize):
  #       if Board[x][y+k] == "X":
  #         Count += 1
  #         if Count == 4:
  #           print("Player 1 Wins")
  #           RestartGame(gridXSize, gridYSize)
  #       else:
  #         Count = 0
  #     if y <= gridYSize:
  #       y += 1 
  
  # for k in range(0, gridYSize):
  #   while k-1 <= gridYSize:
  #     for x ,y in zip(gridXSize,gridYSize):
  #         if Board[x][y+k] == "O":
  #           CountP2 += 1
  #           if CountP2 == 4:
  #             print("Player 2 Wins")
  #             RestartGame(gridXSize, gridYSize)
  #         else:
  #           CountP2 = 0
        
    
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

Menu(gridXSize, gridYSize)
