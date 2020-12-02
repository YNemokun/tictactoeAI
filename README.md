# tictactoeAI
Implementation of Minimax Algorithm on tic tac toe.

This project uses **Python 3**. The older python versions may have problem running "//" in line 65 in tictactoe.py

## Board
![Image of Board](images/Board.jpg)

## Minimax Explanation

The Minimax Algorithm will maximize the score for X and minimize the score for O. This way the AI can choose the optimum move for each player.

Our basic algorithm for the maximum player will be:
```
def maximizer(board, player):
  create an empty dictionary
  for every empty spots on the board:
    place player
    calculate the score of current board
    if there is a winner:
      append the score and its position to a dictionary
    else:
      call the minimizer and get the minimum
      append that minimum
 return the dictionary
```

For example, in a X-to-move situation:

![Image of Board](images/0.png)

First, the Minimax Algorithm will go and explore **every possible moves** on the board. Since tic-tac-toe is a simple game, we do not set a maximum depth for the algorithm. It will stop **when there is a winner or when the board is full**, calculate the value of that board using the utility function (see below), and record the value and its corresponding move in a dictionary.

This algorithm runs recursively, so we will calculate the values from the bottom and return them up the chain, to the board we start with. Here is a visualization:

![Image of Board](images/1.png)

When there is only one result situation, the value and the player's move will automatically pass up to the previous board. 

![Image of Board](images/2.png)

However, when there are more than one board, depends on the player type (max or min), the get_min/get_max functions from the dictionary will *only* return the min/max value and send that up to the previous board. 

For example, Situation A has a value of **-2**: 1 for the winner, 1 for the empty spot, and a scalar -1 for the minimum player (see utility function below). Situation B has a value of **0** which is passed up by the draw state at position 6. Since O player always chooses the move that minimizes the board values, it will pick the move that results in the smallest outcome possible; in this case, when choosing from a dictionary **{4: 0, 6: -2}**, O will pick position 6.

In these images, the selected minium/maximum values are circled in yellow. 

![Image of Board](images/3.png)

![Image of Board](images/4.png)

Finally, the values go back to the first board, and it will return the optimum move based on the values it gathered. In this example, X's best move is at 4. 

## Code Explanation
  ### Game Setup
   We will create a list of three lists, each containing three strings. From top to bottom, left to right, we number each position from 1 to 9. The positions should be as follow:
   
```
   1  2  3
   
   4  5  6
   
   7  8  9
```   
   There are also three chips: X, O, and EMPTY, which are all type string. When the game starts, a new empty board will be created:
   
```
   .  .  .
   
   .  .  .
   
   .  .  .
```

   The other functions are:
   * Positions
      * Convert the number position into indices
      * Return the player at a position
   * Empty or not
      * Check if the position is empty
      * Count the numbers of empty positions
      * Return all empty positions
   * Moves
      * A method for human players to type their moves
      * Place a chip at a certain position
      * Place a chip at a random position
   * Winners
      * Check if the board still has empty spots
      * Return the winner
      
   With these basic functions, we can build a tic-tac-toe game against a random computer.
      
  ### Dictionary
   The two methods will return the first of all max/min values from a dictionary.
   
  ### Maximizer
   The maximizer will maximize the moves for the maximum player, usually X or human.
   
  ### Minimizer
   The minimizer will minimize the moves for the minimun player, usually O or computer.
   
  ### Utility functions
   This function will calculate the values of each position for the current board. 
   We will assign a value for each state of winning: 
   
      wins = 1, draw = 0
      
   The utility function, which is combined in the code, will add the winner value to the numbers of empty positions. If the winner is the minimum player, we will multiply the utility value by -1. [1]
   
      utility = (winning state + empty spots) * (winning player)
      
   For example, in the board below, if X wins immediate, the utility equation should return (1 + 7) * 1 = 8
   
   ![Image of Board](images/Board.jpg)
   
## Game.py

The first two moves are randomly generated to make the program run faster. For now, the file will return a list of winners for each type of game.

![Image of Result](images/result.png)

All the print functions are turned off, or the games should run like this:

![Image of Result](images/Run.png)

There is also an interactive function called AI_human, where the player can play against the AI.

![Image of Result](images/player.png)

When choosing a player, type either "X" or "O", else the code will ask you to try again.

![Image of Result](images/wrong.png)

## Game Analysis


## Footnotes
[1]: Coding an UNBEATABLE Tic Tac Toe AI (Game Theory Minimax Algorithm EXPLAINED) https://youtu.be/fT3YWCKvuQE
