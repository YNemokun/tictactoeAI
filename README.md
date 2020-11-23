# tictactoeAI
Implementation of Minimax Algorithm on tic tac toe.

## Board
![Image of Board](TicTacToe/board.jpg)

## Minimax Explanation

We will assign a value for each state of winning: 
X wins = 1, O wins = -1, draw = 0
The Minimax Algorithm will maximize the score for X and minimize the score for O.
Our basic algorithm for the maximum player will be:
```
def maximizer(state):
  create an empty dictionary
  if there is empty spots on the board:
    place player
    calculate utility
    if there is a winner:
      append the score and its position to a dictionary
    else:
      use the minimizer and get the minimum
      append that minimum
 return the dictionary
```

## Code Explanation
  ### dictionary
    The two methods will returrn the max/min value from a dictionary.
    
  ### maximizer
  ### minimizer
  ### utility functions

## Game File
All the print functions are turned off, or the games should run like this:

![Image of Result](TicTacToe/Run.png)


The first two moves are randomly generated to make the program run faster.

There is also an interactive function called AI_human, where the player can play against the AI.

## Game Analysis
