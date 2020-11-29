# ------------- Global Variables ------------
# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
# If game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Who's turn is it?
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# The main game driver

# Play a game of tic tac toe


def play_game():
    # display initial board
    display_board()
    # While the game is still going
    while game_still_going:
        # function to handle turn and user input
        handle_turn(current_player)
        # check if the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == 'X' or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Handle a single turn of an arbitrary player


def handle_turn(player):
    position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # when we set the global from within the scope of the function we must declare it global
    global winner
    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner

    else:
        # no win
        winner = None
    return


def check_rows():
    # set up global variables
    global game_still_going
    # check if any of the rows are winners and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # any row has a match flag as a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner of X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

    return


def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the columns are winners and not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # any column has a match flag as a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner of X or O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]

    return


def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the diagonal are winners and not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # any diagonal has a match flag as a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner of X or O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]

    return


def check_if_tie():
    return


def flip_player():
    # global variable
    global current_player
    # if current player is x change to o
    if current_player == "X":
        current_player = "O"
    # if current player is o change it to x
    elif current_player == "O":
        current_player = "X"
    return


play_game()


# Board
# Display Board
# play game
# handle turn
# check win
# Check rows
# check columns
# check diagonals
# check tie
# flip player
