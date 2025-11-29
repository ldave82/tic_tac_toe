import random
import os

BOARD_SIZE = 9          # define the 3x3 board size
BASE = '\033[0m'        # original font color
RED = '\033[91m'        # RED font color for 'X'
GREEN = '\033[92m'      # GREEN font color for '0'

# empty board setup with ' '
board = [' '] * BOARD_SIZE

def color(cell):
    # function to color the player marks red 'X' and green 'O'
    if cell == 'X':
        return f'{RED}{cell}{BASE}'
    elif cell == 'O':
        return f'{GREEN}{cell}{BASE}'
    else:
        return cell

def print_board(board):
    # function to print out the given board, 9 list elements to 3x3 grid with header
    header = '    '
    for i in range(1,4):
        header += f'{i}   '
    print(header)

    # note: I used AI to help with print(f'') coding
    line = '  -------------'
    print(line)
    print(f'1 | {color(board[0])} | {color(board[1])} | {color(board[2])} |')
    print(line)
    print(f'2 | {color(board[3])} | {color(board[4])} | {color(board[5])} |')
    print(line)
    print(f'3 | {color(board[6])} | {color(board[7])} | {color(board[8])} |')
    print(line)

def clear_screen():
    # function to clear the screen based on running OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def player_input(board, current_player):
    # function to ask and validate player input 
    # is it a number, is it in range, is it a free cell
    while True:
        print(f'current player =  {color(current_player)}')
        # ask and check for player inputs (row number)
        while True:
            try:
                ir = int(input('input row number (1 - 3): '))
                if ir > 0 and ir < 4:
                    break
                else:
                    print('input not in range')
            except ValueError:
                print('not a number')
        ir = ir - 1     # convert for 0 index

        # ask and check for player inputs (col number)
        while True:
            try:
                ic = int(input('input col number (1 - 3): '))
                if ic > 0 and ic < 4:
                    break
                else:
                    print('input not in range')
            except ValueError:
                print('not a number')
        ic = ic - 1     # convert for 0 index

        cell = (ir * 3) + ic        # calculate element based on row and column

        # check cell availability and mark placement
        if board[cell] != ' ':
            print('cell already taken')
            continue
        else:
            board[cell] = current_player
            break

def switch_player(player):
    # function to switch between players 'X' and 'O'
    if player == 'X':
        return 'O'
    else:
        return 'X'

def board_check(board, player):
    # function to check the board for winning moves for the current player
    win_con = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    # row
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    # column
        [0, 4, 8], [2, 4, 6]                # diagonal
    ]

    # getting all the possible lines (row, col, diag) with positions (0-8)
    for a, b, c in win_con:
        line_mark = [board[a], board[b], board[c]]
        line_pos = [a, b, c]

        # check if has 2 player marks and empty space in line (possible win)
        if line_mark.count(player) == 2 and line_mark.count(' ') == 1:
            for i in line_pos:
                if board[i] == ' ':
                    # print(f'player {color(player)} has a winning move at {i}')      # test
                    return i        # return the position of the empty space

def cpu_move(board):
    # function for the CPU player to make a move
    win_move = board_check(board, 'O')      # check to mark for win
    if win_move != None:
        board[win_move] = 'O'
        return

    block_move = board_check(board, 'X')    # check to mark for block
    if block_move != None:
        board[block_move] = 'O' 
        return

    while True:                             # otherwise random 'O' placement
        i = random.randrange(BOARD_SIZE)
        if board[i] == ' ':
            board[i] = 'O'
            break

def game_win(board):
    # function to check board status and look for winning combinations
    # return True if win con if found
    # note: I used AI to help with the win_con combinations coding
    win_con = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    # row
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    # column
        [0, 4, 8], [2, 4, 6]                # diagonal
    ]

    # check if all 3 marks are the same and not empty cell
    for i in win_con:
        a, b, c = i[0], i[1], i[2]
        if board[a] == board[b] == board[c] and board[a] != ' ':
            print(f'player {color(board[a])} wins')
            return True
    return False

def game_tie(board):
    # function to check for tied game (all cells are marked and no winner)
    if ' ' not in board:
        print('game is tied')
        return True
    return False    

# starting variables
game_on = True          # flag for game status
current_player = 'X'    # starting player is 'X'

clear_screen()
print('this is tic tac toe')

# main game loop
while game_on:
    print_board(board)

    if current_player == 'X':
        player_input(board, current_player)         # get the player input
    else:
        print('CPU player turn')                    # CPU player turn
        cpu_move(board)

    check_win = game_win(board)                     # check for win
    if check_win:
        game_on = False
    else:
        check_tie = game_tie(board)                 # check for tie if no winner
        if check_tie:
            game_on = False
        else:
            current_player = switch_player(current_player)      # switch player if no win and no tie
    if game_on:
        clear_screen()
    else:
        continue

print_board(board)
print('game over, thank you for playing')
