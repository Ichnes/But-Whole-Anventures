import sys
import time
def delay_print(file_name ="Fabula.txt"):
    with open(file_name) as story:
        for line in story:
            for char in line:
                sys.stdout.write("{}".format(char))
                sys.stdout.flush()
                time.sleep(0.01)


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


def character_creation():
    import functions
    creation = False
    player = "@"
    while creation == False:
        print("Choose your class!\n You wanna play as :\n 1)La Soldato\n 2)Maggi \n 3)Cleptoman\n 4)Barbassus")
        player_choose = functions.getch()
        player_choose.isdigit()
        if player_choose == '1':
            print ("\nCongratulations, you choose La Soldato press any key")
            player = "🚶"
            break
        elif player_choose == '2':
            print ("\nCongratulations, you choose Maggi  press any key")
            player = "🎩"
            break
        elif player_choose == '3':
            print ("\nCongratulations, you choose Cleptoman  press any key")
            player = "👳"
            break
        elif player_choose == '4':
            print ("\nCongratulations, you choose Barbassus  press any key")
            player = "🕵️"
            break
        else:
            print("\nplease, choose only 1,2,3 or 4")
            creation = False
    return player
