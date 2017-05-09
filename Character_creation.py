soldato_items = ['gun']
maggi_items = ['wand', 'banana']
cleptoman_items = ['wallet', 'knife']
barbassus_item = ['sword', 'life potion', 'helmet']
character = {'La Soldato' : soldato_items, 'Maggi' : maggi_items, "Cleptoman" : cleptoman_items, 'Barbassus' : barbassus_item}

print (character)


def character_creation():
    creation = False
    while creation == False:
        print("Choose your class!\n You wanna play as :\n 1)La Soldato\n 2)Maggi \n 3)Cleptoman\n 4)Barbassus")
        player_choose = input('Press 1-4 to choose class: ')
        player_choose.isdigit()
        if player_choose == '1':
            print ("\nCongratulations, you choose La Soldato")
            break
        elif player_choose == '2':
            print ("\nCongratulations, you choose Maggi")
            break
        elif player_choose == '3':
            print ("\nCongratulations, you choose Cleptoman")
            break
        elif player_choose == '4':
            print ("\nCongratulations, you choose Barbassus")
            break
        else:
            print("\nplease, choose only 1,2,3 or 4")
            creation = False
            return creation

def la_soldato():



def maggi():


def cleptoman():


def barbassus():


character_creation()
