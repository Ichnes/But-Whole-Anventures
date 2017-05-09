from random import randint
import os
import functions

def create_board(filename="mapa.txt"):
    with open("mapa.txt","r") as mapa:
        the_map_list = []
        for line in mapa.readlines():
            list_of_chars = []
            for char in line:
                if char != "\n":
                    list_of_chars.append(char)
            the_map_list.append(list_of_chars)
    return the_map_list

def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()

def wsad(board, char, x_pos, y_pos):
    board[x_pos][y_pos] = " "
    movable_items = [" ","💩","♥"]
    if char == 'd' and  board[x_pos][y_pos +1] in movable_items:
        y_pos += 1
    elif char == 'a' and board[x_pos][y_pos - 1] in movable_items:
        y_pos -= 1
    elif char == 'w' and board[x_pos - 1][y_pos] in movable_items:
        x_pos -= 1
    elif char == 's' and board[x_pos + 1][y_pos] in movable_items:
        x_pos += 1
    elif char == "p":
        exit()
    return board, x_pos, y_pos



def insert_player(board, x_pos, y_pos,player):
    board[x_pos][y_pos] = player
    return board


def main():
    char = ''
    x_pos = 1
    y_pos = 1
    board = create_board()
    functions.delay_print("Fabula.txt")
    player = functions.character_creation()
    while True:
        char = functions.getch()
        board,x_pos, y_pos = wsad(board,char, x_pos, y_pos)
        board_with_player = insert_player(board, x_pos, y_pos,player)
        os.system('clear')
        print_board(board_with_player)
        print("y:", x_pos)
        print("x", y_pos)

main()
