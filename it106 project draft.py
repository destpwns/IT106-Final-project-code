import random

def starting_menu():
    print("Welcome to Gauntlet, the game where you face endless monsters with increasing difficulty.")
    while True:
        option = input("Would you like to play? Y/N? ")
        if option.lower() == "y" or option.lower() == "Y":
            print("Good choice.")
            return
        else:
            print("You are exiting Gauntlet.")
            break
    
def player():
    playerName = {}
    while True:
        name = input("What is your name? ")
        playerName.append(name)
        print("Your character's name is: ", playerName)
        return
    
def spell_dictionary():
    meleeSpells = {
        "Slash": {3, 5, 7, 9},  
        "Stab": {3, 5, 7, 9},   
        "Sweep": {3, 5, 7, 9}
    }
    magicSpells = {
        "Lightning Strike": {3, 5, 7, 9}, 
        "Fireball": {3, 5, 7, 9}, 
        "Water Cannon": {3, 5, 7, 9}, 
        "Boulder Crush": {3, 5, 7, 9}
    }
    
def main():
    starting_menu()
    player()
    spell_dictionary()
    
main()