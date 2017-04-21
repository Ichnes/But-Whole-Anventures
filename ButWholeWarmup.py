from random import randint
from time import sleep
import os

def create_board(width, height):
    board = []
    for row in range(0,height):
        board_row = []
        for column in range(0,width):
            if row == 0 or row == height-1:
                board_row.append('X')
            else:
                if column == 0 or column == height-1:
                    board_row.append('X')
                else:
                    board_row.append(' ')
        board.append(board_row)
    return board

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch



def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()

def wsad(board, char, x_pos, y_pos):
    if char == 's' and  " " in board[x_pos][y_pos +1]:
        y_pos += 1
    elif char == 'w' and " " in board[x_pos][y_pos - 1]:
        y_pos -= 1
    elif char == 'a' and " "  in board[x_pos - 1][y_pos]:
        x_pos -= 1
    elif char == 'd' and " "  in board[x_pos + 1][y_pos]:
        x_pos += 1
    elif char == "p":
        exit()
    return x_pos, y_pos



def insert_player(board, width, height):
    board[height][width] = '@'
    return board


def main():
    char = ''
    x_pos = 10
    y_pos = 10
    while True:
        char = getch()
        board = create_board(20, 20)
        x_pos, y_pos = wsad(board,char, x_pos, y_pos)
        board_with_player = insert_player(board, x_pos, y_pos)
        os.system('clear')
        print_board(board_with_player)



main()
