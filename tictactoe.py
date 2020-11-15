#TIC TAC TOE
import math                                    #import math library to use infinity

from random import random

infinity = math.inf

game_board = ["_" for x in range(10)]          #gameboard as a global list
game_board[0] = -1                             #the first index will hold action value

def insertLetter(letter,pos):
  game_board[pos] = letter

def spaceIsFree(pos):                           #checks for any available spots on game board
  return game_board[pos] == '_'

def printBoard(game_board):
  print(game_board[1] + " | " + game_board[2] + " | " + game_board[3])
  print(game_board[4] + " | " + game_board[5] + " | " + game_board[6])
  print(game_board[7] + " | " + game_board[8] + " | " + game_board[9])

def isWinner(st,ply):
  return (st[7] == ply and st[8] == ply and st[9] == ply) or (st[4] == ply and st[5] == ply and st[6] == ply) or (st[1] == ply and st[2] == ply and st[3] == ply) or (st[1] == ply and st[4] == ply and st[7] == ply) or (st[2] == ply and st[5] == ply and st[8] == ply) or (st[3] == ply and st[6] == ply and st[9] == ply) or (st[1] == ply and st[5] == ply and st[9] == ply) or (st[3] == ply and st[5] == ply and st[7] == ply) 

def game_over(state):
  return isWinner(state,'X') or isWinner(state,'O') or isBoardFull(state)

def num_empty_spaces(board):
  return board.count('_')

def empty_spot_indices(board):                              #returns list of available spaces on board
  list1 = [i for i,le in enumerate(board) if le == '_']
  #list1.remove(0)
  return list1

def isBoardFull(board):
  if board.count('_') >= 1:
    return False
  else:
    return True

def about_to_win():
  av_spots = empty_spot_indices(game_board)
  state = game_board
  for i in av_spots:
    state[i] = "X"
    if (isWinner(state,"X")):
      return [True,i]
    state[i] = "_"
  return [False,-1]

def evaluate(board):                              #returns utility value of any state 
  if(isWinner(board,'O')):
    return 1
  elif(isWinner(board,'X')):
    return -1
  else:
    if(isBoardFull(board)):
      return 0

def miniMax(board):                               #miniMax function to find best action against an optimal opponent for DIFFICULT level
  depth = num_empty_spaces(board)

  def maxValue(Depth,State):
    best = [-1,-infinity]
    if Depth == 0 or game_over(State):
      util_val = evaluate(State)
      return [State[0],util_val]
    available_spots = empty_spot_indices(State)
    for i in available_spots:
      State[0] = i
      State[i] = "O"
      value = minValue(Depth-1,State)
      State[i] = "_"
      if value[1] > best[1]:
        best[1] = value[1]
        best[0] = i
    return best

  def minValue(Depth,State):
    best = [-1,infinity]
    if Depth == 0 or game_over(State):
      util_val = evaluate(State)
      return [State[0],util_val]
    available_spots = empty_spot_indices(State)
    for i in available_spots:
      State[0] = i
      State[i] = "X"
      value = maxValue(Depth-1,State)
      State[i] = "_"
      if value[1] < best[1]:
        best[1] = value[1]
        best[0] = i
    return best

  move = maxValue(depth,board)
  return move                                        #returns a list in format [action, utility value]

def rcompMove():                                     #function for EASY level. Generated random legal actions
  move = 0
  center = 5
  if (spaceIsFree(center)):
    return center
  while not(spaceIsFree(move)) or (move == 0):
    move = int(random()*9)
  return move

def icompMove():                                      #function for intermediate level, avoids possible winning of opponent
  outer_corners = [1,3,7,9]
  value = about_to_win()
  av_spots = empty_spot_indices(game_board)
  if (value[0]):
    return value[1]
  elif not(value[0]):
    for i in outer_corners:
      if (spaceIsFree(i)):
        return i
  else:
    for i in empty_spot_indices:
    if(spaceIsFree(i)):
        return i

def compMove():
  board = game_board
  move = miniMax(board)
  return move[0]

def playerMove():
  run = True
  while run:
    move = input("\nPlease select a position to place an 'X' (1-9): ")
    try:
      move = int(move)
      if move > 0 and move < 10:
        if spaceIsFree(move):
          run = False
          insertLetter('X',move)
        else:
          print("This space is occupied.")
      else:
        print("Please enter a number between (1-9)")
    except: 
      print("Please type a number between (1-9).")

def main():
  print("Let's play TIC TAC TOE!")
  printBoard(game_board)
  choice = int(input("Choose level: \n1.Easy\n2.Intermediate\n3.Difficult\n"))
  if (choice == 3):
    print("\nMeet the UNBEATABLE OPPONENT!!")
    while not(isBoardFull(game_board)):
      if not(isWinner(game_board,'O')):
        playerMove()
      else:
        print('Haha! The Computer won this time!')
        printBoard(game_board)
        break
      if not(isWinner(game_board,'X')):
        move = compMove()
        insertLetter('O',move)
        printBoard(game_board)
        print(f"Computer placed an 'O' in position {move}:")
      else:
        print('Congratulations! You won this time!')
        printBoard(game_board)
        break

    if isBoardFull(game_board):
      print("There's a tie!")

  if (choice == 2):
    print("\nThis might be slightly difficult...")
    while not(isBoardFull(game_board)):
      if not(isWinner(game_board,'O')):
        playerMove()
      else:
        print('Haha! The Computer won this time!')
        printBoard(game_board)
        break
      if not(isWinner(game_board,'X')):
        if not(isBoardFull(game_board)):
          move = icompMove()
          insertLetter('O',move)
          printBoard(game_board)
          print(f"Computer placed an 'O' in position {move}:")
      else:
        print('Congratulations! You won this time!')
        printBoard(game_board)
        break

    if isBoardFull(game_board):
      print("There's a tie!")

  elif (choice == 1):
    print("\nThis should be pretty easy!!")
    while not(isBoardFull(game_board)):
      if not(isWinner(game_board,'O')):
        playerMove()
      else:
        print('Haha! The Computer won this time!')
        printBoard(game_board)
        break
      if not(isWinner(game_board,'X')):
        move = rcompMove()
        insertLetter('O',move)
        printBoard(game_board)
        print(f"Computer placed an 'O' in position {move}:")
      else:
        print('Congratulations! You won this time!')
        printBoard(game_board)
        break

    if isBoardFull(game_board):
      printBoard(game_board)
      print("There's a tie!")

main()
