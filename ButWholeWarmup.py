from random import randint
import os
import functions
import time
class Colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def create_board(filename="mapa.txt"):
    with open(filename,"r") as mapa:
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
            if char == "♥":
                char = Colour.RED + "♥" + Colour.END
            elif char == "💩":
                char == Colour.GREEN + "💩" + Colour.END
            elif char == "💣":
                char == Colour.YELLOW + "💣" + Colour.END
            print(char, end='')
        print()

def wsad(board, char, x_pos, y_pos):
    board[x_pos][y_pos] = " "
    movable_items = [" ","💩","♥","💣"]
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


def level_1():
    global inv
    life = 100
    char = ""
    x_pos = 1
    y_pos = 1
    board = create_board()
    #functions.delay_print("Fabula.txt")
    #time.sleep(1)
    #os.system('clear')
    while char!= "p":
        if board[18][34] == player:
            os.system('clear')
            return
        if life <= 0:
            os.system('clear')
            print("GAME OVER")
            return
        char = functions.getch()
        board,x_pos, y_pos = wsad(board,char, x_pos, y_pos)
        life,inv = functions.interaction_with_items(life,inv,board,x_pos,y_pos)

        board_with_player = insert_player(board, x_pos, y_pos,player)
        os.system('clear')
        print_board(board_with_player)
        print("y:", x_pos)
        print("x", y_pos)
        print(inv, "   życie: " ,life)

def level_2():
    global inv
    life = 100
    char = ""
    x_pos = 1
    y_pos = 1
    board = create_board("mapa2.txt")
    #functions.delay_print("Fabula.txt")
    #time.sleep(1)
    #os.system('clear')
    while char!= "p":
        '''if board[18][34] == player:
            os.system('clear')
            return'''
        if life <= 0:
            os.system('clear')
            print("GAME OVER")
            return
        char = functions.getch()
        board,x_pos, y_pos = wsad(board,char, x_pos, y_pos)
        life,inv = functions.interaction_with_items(life,inv,board,x_pos,y_pos)

        board_with_player = insert_player(board, x_pos, y_pos,player)
        os.system('clear')
        print_board(board_with_player)
        print("y:", x_pos)
        print("x", y_pos)
        print(inv, "   życie: " ,life)


player = functions.character_creation()
os.system("clear")
inv = {"money":0,"poo":0,"secret key":0,""}
#level_1()
#os.system('clear')
level_2()
