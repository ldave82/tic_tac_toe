# import random

BOARD_SIZE = 9
BASE = '\033[0m'        # original font color
RED = '\033[91m'        # RED font color for 'X'
GREEN = '\033[92m'      # GREEN font color for '0'

board = [' '] * BOARD_SIZE

def print_board(board):
    def color(cell):
        if cell == 'X':
            return f'{RED}{cell}{BASE}'
        elif cell == 'O':
            return f'{GREEN}{cell}{BASE}'
        else:
            return cell
    
    header = '    '
    for i in range(1,4):
        header += f'{i}   '
    print(header)

    line = '  -------------'
    print(line)
    print(f'1 | {color(board[0])} | {color(board[1])} | {color(board[2])} |')
    print(line)
    print(f'2 | {color(board[3])} | {color(board[4])} | {color(board[5])} |')
    print(line)
    print(f'3 | {color(board[6])} | {color(board[7])} | {color(board[8])} |')
    print(line)

game_on = True
current_player = 'X'

def player_input(board, current_player):
    while True:
        print('current player = ' + current_player)
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

        cell = (ir * 3) + ic

        if board[cell] != ' ':
            print('cell already taken')
            continue
        else:
            board[cell] = current_player
            break

def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def game_win(board):
    win_con = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    # row
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    # column
        [0, 4, 8], [2, 4, 6]                # diagonal
    ]

    for i in win_con:
        a, b, c = i[0], i[1], i[2]
        if board[a] == board[b] == board[c] and board[a] != ' ':
            if board[a] == 'X':
                color = RED
            else:
                color = GREEN
            print(f'player {color}{board[a]}{BASE} wins')
            return True
    return False

def game_tie(board):
    if ' ' not in board:
        print('game is tied')
        return True
    return False    

while game_on:
    print_board(board)

    player_input(board, current_player)
    check_win = game_win(board)
    if check_win:
        game_on = False
    else:
        check_tie = game_tie(board)
        if check_tie:
            game_on = False
        else:
            current_player = switch_player(current_player)

print_board(board)
print('game over, thank you for playing')
