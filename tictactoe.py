"""
Tic Tac Toe Module
"""

# ==============================================
import random as rnd
import copy
from dictionary import get_max_key
from dictionary import get_min_key

# ==============================================


X = "X"
O = "O"
EMPTY = "."
"""
Main components of the game: players and board
"""
game_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def new_board():
    """
    Set up an empty board
    :return: a list of three lists, each consists of three players
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def show_board(board):
    """
    Print out the board
    :param board: current board input
    :return: strings
    """
    print("")
    for row in board:
        for cell in row:
            print(cell + " ", end='')
        print("")
    print("")


def opponent(player):
    """
    Find the opponent player
    :param player: X, O, or EMPTY
    :return: a player
    """
    if player == X:
        return O
    elif player == O:
        return X
    else:
        return EMPTY


def rowFromPos(pos):
    """
    convert the 1-9 position to indices
    :param pos: 1-9
    :return: the corresponding row
    """
    return (pos - 1) // 3


def colFromPos(pos):
    """
    convert the 1-9 position to indices
    :param pos: 1-9
    :return: the corresponding column
    """
    return (pos - 1) % 3


def whoIsAt(board, p):
    """
    Get the player at a position
    :param board: current board
    :param p: 1-9 position
    :return: a player
    """
    return board[rowFromPos(p)][colFromPos(p)]


def isEmpty(board, p):
    """
    Check if the position is EMPTY
    :param board:
    :param p: 1-9 position
    :return: a boolean
    """
    return whoIsAt(board, p) == EMPTY


def possibleSpots(cboard=game_board):
    """
    Return all empty spots
    :param cboard:
    :return: a list of integers
    """
    result = []
    for i in range(1, 10):
        if isEmpty(cboard, i):
            result.append(i)
    return result


def player_moves():
    """
    Receive a keyboard input from human
    :return: 1-9 position
    """
    print("player")
    while True:
        try:
            move = int(input(f"Type in your move({possibleSpots()}):"))
            if move not in possibleSpots():
                print("Choose another answer")
            else:
                return move
        except:
            print("Choose again")


def count_empty(cboard):
    """
    Count the numbers of empty spots
    :param cboard:
    :return: an integer
    """
    result = 0
    for i in range(1, 10):
        if isEmpty(cboard, i):
            result += 1
    return result


def placePlayer(board, player, pos):
    """
    Put a player on the board at a position
    :param board:
    :param player:
    :param pos:
    :return: set the position to the player
    """
    if isEmpty(board, pos):
        board[rowFromPos(pos)][colFromPos(pos)] = player


def choosePlayer():
    """
    Choosing player for human before the game starts
    :return: two players with their corresponding identity
    """
    while True:
        human = input("Play as X/O:")
        if human != X and human != O:
            print("Wrong input, try again")
        else:
            if human == "X":
                player1 = "h"
                player2 = "c"
            elif human == "O":
                player2 = "h"
                player1 = "c"
                # print(f'You are {human_player}')
            print(f'You are {human}')
            return player1, player2


def hasMoves(board):
    """
    Check if there is move on the board
    :param board:
    :return: a boolean
    """
    for p in range(1, 10):
        if isEmpty(board, p):
            return True
    return False


def randOpenMove(board):
    """
    Generate a random integer position
    :param board:
    :return: a random integer position from 1-9
    """
    moves = []
    for p in range(1, 10):
        if isEmpty(board, p):
            moves.append(p)
    return moves[rnd.randrange(len(moves))]


def checkForWinner(board):
    """
    Check if there is a winner on the board
    :param board:
    :return: a player that is a winner
    """
    # col check...
    for p in range(1, 4):
        if not isEmpty(board, p):
            if (whoIsAt(board, p) == whoIsAt(board, p + 3)) and (whoIsAt(board, p) == whoIsAt(board, p + 6)):
                return whoIsAt(board, p)
    # row check...
    for p in range(1, 8, 3):
        if not isEmpty(board, p):
            if (whoIsAt(board, p) == whoIsAt(board, p + 1)) and (whoIsAt(board, p) == whoIsAt(board, p + 2)):
                return whoIsAt(board, p)

    if not isEmpty(board, 1):
        if (whoIsAt(board, 1) == whoIsAt(board, 5)) and (whoIsAt(board, 1) == whoIsAt(board, 9)):
            return whoIsAt(board, 1)

    if not isEmpty(board, 3):
        if (whoIsAt(board, 3) == whoIsAt(board, 5)) and (whoIsAt(board, 3) == whoIsAt(board, 7)):
            return whoIsAt(board, 3)

    return EMPTY


# =========================================================================================
#  Min Max functions here ................................
# =========================================================================================

def maximize_move(board, player):
    """
    Return the values each move gets
    :param board:
    :param player:
    :return: a dictionary of values with indices
    """
    scores = {}
    for p in range(1, 10):
        tmpBoard = copy.deepcopy(board)
        if isEmpty(tmpBoard, p):
            placePlayer(tmpBoard, player, p)
            winner = checkForWinner(tmpBoard)
            factor = count_empty(tmpBoard) + 1
            if winner == player:
                scores[p] = (1 * factor)

            else:
                if hasMoves(tmpBoard):
                    moves = minimize_move(tmpBoard, player)
                    m = get_min_key(moves)
                    scores[p] = moves[m]
                else:
                    scores[p] = 0

    return scores


def minimize_move(board, player):
    """
    Return the values each move gets
    :param board:
    :param player:
    :return: a dictionary of values with indices
    """
    scores = {}
    for p in range(1, 10):
        tmpBoard = copy.deepcopy(board)
        if isEmpty(tmpBoard, p):
            placePlayer(tmpBoard, opponent(player), p)
            winner = checkForWinner(tmpBoard)
            factor = count_empty(tmpBoard) + 1
            if winner == opponent(player):
                scores[p] = (-1 * factor)

            else:
                if hasMoves(tmpBoard):
                    moves = maximize_move(tmpBoard, player)
                    m = get_max_key(moves)
                    scores[p] = moves[m]
                else:
                    scores[p] = 0

    return scores


# Start the game ================================


def AI_AI(trials=1):
    """
    trials between two AIs
    :param trials:
    :return: a list of winners
    """
    winners = []
    while trials > 0:
        game_board = new_board()
        winner = EMPTY
        xTurn = True

        placePlayer(game_board, X, randOpenMove(game_board))
        placePlayer(game_board, O, randOpenMove(game_board))
        # show_board(game_board)

        while hasMoves(game_board) and winner == EMPTY:
            if xTurn:
                s = maximize_move(game_board, X)
                # print("X move values : ", s)
                m = get_max_key(s)
                # print("move is : ", m)
                placePlayer(game_board, X, m)
            else:
                s = maximize_move(game_board, O)
                # print("O move values : ", s)
                m = get_max_key(s)
                # print("move is : ", m)
                placePlayer(game_board, O, m)

            winner = checkForWinner(game_board)
            # show_board(game_board)

            xTurn = not xTurn

        # print("Game over")
        if winner is not EMPTY:
            # print(winner + " is the winner")
            winners.append(winner)
        else:
            # print("It is a tie...")
            winners.append(EMPTY)
        trials -= 1
    return winners


def AI_human(trials=1):
    """
    trials between AI and human
    :param trials: ask for inputs
    :return: a list of winners
    """
    winners = []
    while trials > 0:
        game_board = new_board()
        winner = EMPTY
        player1, player2 = choosePlayer()
        xTurn = True
        placePlayer(game_board, X, randOpenMove(game_board))
        placePlayer(game_board, O, randOpenMove(game_board))
        # show_board(game_board)

        while hasMoves(game_board) and winner == EMPTY:
            if xTurn:
                player = player1
                chip = X
            else:
                player = player2
                chip = O

            if player == "c":
                s = maximize_move(game_board, chip)
                print("X move values : ", s)
                m = get_max_key(s)
                print("move is : ", m)
                placePlayer(game_board, chip, m)
            else:
                placePlayer(game_board, chip, player_moves())

            winner = checkForWinner(game_board)
            show_board(game_board)

            xTurn = not xTurn
        print("Game over")
        if winner is not EMPTY:
            print(winner + " is the winner\n")
            winners.append(winner)
        else:
            print("It is a tie...\n")
            winners.append(EMPTY)
    return winner


def random_generate(trials=1):
    """
    generate trials with random moves
    :param trials:
    :return: a list of winners
    """
    winners = []
    while trials > 0:
        game_board = new_board()
        winner = EMPTY
        xTurn = True
        # show_board(game_board)

        while hasMoves(game_board) and winner == EMPTY:
            if xTurn:
                player = X
            else:
                player = O

            placePlayer(game_board, player, randOpenMove(game_board))
            winner = checkForWinner(game_board)
            # show_board(game_board)

            xTurn = not xTurn

        # print("Game over")
        if winner is not EMPTY:
            # print(winner + " is the winner")
            winners.append(winner)
        else:
            # print("It is a tie...")
            winners.append(EMPTY)
        trials -= 1
    return winners


def AI_random(trials=1):
    """
    AI play against a random position generator
    :param trials:
    :return: a list of winners
    """
    winners = []
    while trials > 0:
        game_board = new_board()
        winner = EMPTY
        xTurn = True
        # show_board(game_board)

        placePlayer(game_board, X, randOpenMove(game_board))
        placePlayer(game_board, O, randOpenMove(game_board))
        # show_board(game_board)
        while hasMoves(game_board) and winner == EMPTY:
            if xTurn:
                s = maximize_move(game_board, X)
                # print("X move values : ", s)
                m = get_max_key(s)
                # print("move is : ", m)
                placePlayer(game_board, X, m)
            else:
                placePlayer(game_board, O, randOpenMove(game_board))

            winner = checkForWinner(game_board)
            # show_board(game_board)

            xTurn = not xTurn

        # print("Game over")
        if winner is not EMPTY:
            # print(winner + " is the winner")
            winners.append(winner)
        else:
            # print("It is a tie...")
            winners.append(EMPTY)
        trials -= 1
    return winners


def random_AI(trials=1):
    """
    AI play against a random position generator
    :param trials:
    :return: a list of winners
    """
    winners = []
    while trials > 0:
        game_board = new_board()
        winner = EMPTY
        xTurn = True
        # show_board(game_board)

        placePlayer(game_board, X, randOpenMove(game_board))
        placePlayer(game_board, O, randOpenMove(game_board))
        # show_board(game_board)
        while hasMoves(game_board) and winner == EMPTY:
            if not xTurn:
                s = minimize_move(game_board, O)
                # print("X move values : ", s)
                m = get_min_key(s)
                # print("move is : ", m)
                placePlayer(game_board, O, m)
            else:
                placePlayer(game_board, X, randOpenMove(game_board))

            winner = checkForWinner(game_board)
            # show_board(game_board)

            xTurn = not xTurn

        # print("Game over")
        if winner is not EMPTY:
            # print(winner + " is the winner")
            winners.append(winner)
        else:
            # print("It is a tie...")
            winners.append(EMPTY)
        trials -= 1
    return winners


"""
The testing trials. Remember to comment these out if this file is used as a module.
"""
# print(random_generate(10))
# print(AI_human())
# print(AI_AI(10))
# print(AI_random(10))
# print(random_AI(10))
