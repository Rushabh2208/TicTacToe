import random

global player_1_marker, player_2_marker, board, playAgain
playAgain = 1


def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_input():
    global player_1_marker, player_2_marker

    while True:
        print("Player 1 select a marker 'X' or '0':  ")
        player_1_marker = input()
        if player_1_marker == 'X' or player_1_marker == 'O':
            break

    if player_1_marker == 'X':
        player_2_marker = 'O'
    else:
        player_2_marker = 'X'

    print("Player 1 is: ", player_1_marker)
    print("Player 2 is: ", player_2_marker)


def place_marker(board, marker, position):
    board[position - 1] = marker


def win_check(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    if board[0] == mark and board[3] == mark and board[6] == mark:
        return True
    if board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    if board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    if board[8] == mark and board[7] == mark and board[6] == mark:
        return True
    if board[2] == mark and board[4] == mark and board[6] == mark:
        return True
    if board[3] == mark and board[4] == mark and board[5] == mark:
        return True


def choose_first():
    return random.randint(1, 2)


def space_check(board, position):
    if board[position - 1] != " ":
        return False
    else:
        return True


def full_board_check(board):
    for space in board:
        if space == " ":
            return True

    return False


def replay():
    print("Want to Play Again")
    response = input()
    if response[0] == 'y' or response[0] == 'Y':
        return True
    else:
        return False


while True:
    print("Welcome to Tic Tac Toe game")
    global board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    display_board(board)
    player_input()
    play = choose_first()
    keepPlaying = True
    while (play == 1 or play == 2) and keepPlaying:
        print("Player {play} enter the position: ".format(play=play))
        marker_position = int(input())
        while marker_position not in range(1, 10):
            print("Player {play} enter the position: ".format(play=play))
            marker_position = int(input())
        else:
            if space_check(board, marker_position):
                if play == 1:
                    place_marker(board, player_1_marker, marker_position)
                    if win_check(board, player_1_marker):
                        display_board(board)
                        print("Player {x} wins".format(x=play))
                        keepPlaying = False
                    else:
                        display_board(board)
                        play = 2
                        keepPlaying = full_board_check(board)

                else:
                    place_marker(board, player_2_marker, marker_position)
                    if win_check(board, player_2_marker):
                        display_board(board)
                        print("Player {x} wins".format(x=play))
                        keepPlaying = False
                    else:
                        display_board(board)
                        play = 1
                        keepPlaying = full_board_check(board)

            else:
                print("The space is already occupied")
    else:
        if replay():
            pass
        else:
            exit()
