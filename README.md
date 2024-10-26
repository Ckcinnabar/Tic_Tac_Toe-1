# Tic-tac-toe Game

A simple command-line implementation of the classic Tic-tac-toe game written in Python.

## Description

This program implements a two-player Tic-tac-toe game where players take turns placing their marks (X or O) on a 3x3 grid. The game features input validation, win detection, and the ability to play multiple rounds.

## Features

- Interactive command-line interface
- 3x3 game board with coordinate system
- Alternating turns between X and O players
- Input validation for:
  - Valid coordinate ranges (0-2)
  - Already occupied cells
  - Proper input format (row,column)
- Win detection for:
  - Horizontal rows
  - Vertical columns
  - Diagonals
- Draw detection when board is full
- Option to play multiple games

## How to Play

1. The game starts with player X's turn
2. Enter coordinates as "row,column" (e.g., "1,1" for center)
3. Coordinates range from 0 to 2
4. Players alternate turns until someone wins or the game is a draw
5. After each game, you can choose to play again

## Input Format
- Use comma-separated values for row and column
- Example: "0,0" for top-left corner
- Valid range: 0-2 for both row and column

## Game Rules
- Players take turns placing their marks (X or O)
- First player to get three of their marks in a row (horizontal, vertical, or diagonal) wins
- If the board fills up with no winner, the game is a draw

## Example Board Layout
```
R\C |  0  |  1  |  2  | 
-----------------------
 0  |     |     |     | 
-----------------------
 1  |     |     |     | 
-----------------------
 2  |     |     |     | 
-----------------------
```

## Error Handling
- Invalid coordinates will prompt for re-entry
- Attempting to place a mark in an occupied cell will prompt for a new selection
- Incorrect input format will ask for proper comma-separated values

## Author
Kuan Chen Chen

## Date
September 23, 2024

## Version
1.0
