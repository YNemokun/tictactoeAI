# tictactoeAI
Implementation of Minimax Algorithm on tic tac toe.

## Board
![Image of Board](Board.jpg)

## Minimax Explanation

The Minimax Algorithm will maximize the score for X and minimize the score for O. This way the AI can choose the optimum move for each player.
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
    The maximizer will maximize the moves for the maximum player, usually X or human.
  ### minimizer
    The minimizer will minimize the moves for the minimun player, usually O or computer.
  ### utility functions
    This function will calculate the values of each position for the current board. 
    We will assign a value for each state of winning: 
    X wins = 1, O wins = -1, draw/game continued = 0
    The utility function, which is combined in the code, will add the stae value to the numbers of empty positions (reference: https://youtu.be/fT3YWCKvuQE)

## Game File
All the print functions are turned off, or the games should run like this:

![Image of Result](TicTacToe/Run.png)


The first two moves are randomly generated to make the program run faster.

There is also an interactive function called AI_human, where the player can play against the AI.

## Game Analysis
