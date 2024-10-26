# -*- coding: utf-8 -*-
"""KC_Tic_Tac_Toe.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZPv4v-pf9tpPwhsJDkQASFHvcGfPAqZE

# Kuan Chen Chen Tic_Tac_Toe
## Made by: 2024/9/23 12:08AM
## Project instruction:
### Playing Tic-Tac-Toe by enter the avalible input.If enter invalid input the program will tell you to enter the correct one,the program will also detect the win or tie, and the user can choose to end the game or repeat the game again and again.
"""

def printBoard(board):
    for row in board:
        print(" | ".join(row)+" | ")
        print("-----------------------")

# Draw the line of the board

def checkFull(board):
    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] == "   ":
                return False
    return True

    # Check if the board is full

def validateEntry(row, col, board):
    if 1 <= row <= 3  and  1 <= col <= 3:
      if board[row][col] != "   ":
        print("That cell is already taken.\nPlease make another selection.")
        return False
        # If the input is valid but the position is not "   " means the cell is already been taken

      else:
        return True

    print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
    # Invalid entry, the input is not on the board

    return False

def checkWin(board, turn):
    for i in range(1, 4):
        if board[i][1] == board[i][2] == board[i][3] == f" {turn} ":
            return True
            # We check the column win

    for j in range(1, 4):
        if board[1][j] == board[2][j] == board[3][j] == f" {turn} ":
            return True
            # We check the row win

    if board[1][1] == board[2][2] == board[3][3] == f" {turn} ":
        return True
        # We check top-left to bottom-right


    if board[1][3] == board[2][2] == board[3][1] == f" {turn} ":
        return True
        # We check top-right to bottom-right

    return False
    # If no win condition is met, return False

def main():
  turn = 'X'
  board = [
      ["R\C", " 0 ", " 1 ", " 2 "],
      [" 0 ", "   ", "   ", "   "],
      [" 1 ", "   ", "   ", "   "],
      [" 2 ", "   ", "   ", "   "]
  ]
  # We have to make a board at first, and each time we repeat the game, the board will renew itself


  print("New Game: X goes first.\n")
  print("-"*23)
  printBoard(board)

  while True:
      print(f"\n{turn}'s turn.")
      print(f"Where do you want your {turn} placed?")

      user_input = input("Please enter row number and column number separated by a comma.\n").split(",")
      # We split the input into element separated by comma

      user_input = [item.strip() for item in user_input if item.strip()]
      # Remove any leading or trailing spaces from each element in the user_input list, and filter out any empty elements

      if len(user_input) != 2:
        print("Invalid input. Please enter exactly two numbers separated by a comma.")
        continue
      # If the input is not (x,y),EX(x,y,z) we loop again until the right input.


      row, col = map(int, user_input)

      row += 1
      col += 1
      # Because the first row and column of the board is the label, so we have to +1 to the input to place them in the right place

      if validateEntry(row, col, board)==False:
          continue
      # Check the input is valid

      print(f"You have entered row #{row-1} \n          and column #{col-1}")
      print("Thank you for your selection.")
      board[row][col] = f" {turn} "
      # Replace the "   " into X/O

      if checkWin(board, turn) == True:
          print(f"{turn} IS THE WINNER!!!")
          printBoard(board)
          break
      # We check the win first, because theres might be case that after the last placed, the board is full and X/O wins the game
      # So if we check the win first, if theres a win then the code will break the loop.

      if checkFull(board) == True:
          print("DRAW! NOBODY WINS!!")
          printBoard(board)
          break
      print("-"*23)
      printBoard(board)

      turn = 'X' if turn == 'O' else 'O'
      # Change the turn

repeat = 'yes'
while repeat[0].lower() == 'y':
  main()
  repeat = input("\nAnother game? Enter Y or y for yes.\n")
  # The repeat of the game.

print("Thank you for playing!")

