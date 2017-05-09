from random import randint

player_moves = ["ROCK", "PAPER", "SCISSORS"]

computer_moves = player_moves[randint(0,2)]

player = False

while player == False:
#set player to False
    player = input("Rock, Paper, Scissors?").upper()
    if player in player_moves:
        if player == computer_moves:
            print("Tie!")
            print("Let's play again")
            player = False
            computer_moves = player_moves[randint(0,2)]
        elif player == "Rock":
            if computer_moves == "Paper":
                print("You lose!", computer_moves, "covers", player)
                print("Let's play again")
                player = False
                computer_moves = player_moves[randint(0,2)]
            else:
                print("You win!", player, "smashes", computer_moves)
        elif player == "Paper":
            if computer_moves == "Scissors":
                print("You lose!", computer_moves, "cut", player)
                print("Let's play again")
                player = False
                computer_moves = player_moves[randint(0,2)]
            else:
                print("You win!", player, "covers", computer_moves)
        elif player == "Scissors":
            if computer_moves == "Rock":
                print("You lose...", computer_moves, "smashes", player)
                print("Let's play again")
                player = False
                computer_moves = player_moves[randint(0,2)]
            else:
                print("You win!", player, "cut", computer_moves)
        else:
            print("That's not a valid play. Check your spelling!")
            player = False
            computer_moves = player_moves[randint(0,2)]
    else:
        print("invalid input")
        player = False
