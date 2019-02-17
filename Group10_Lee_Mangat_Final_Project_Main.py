import random
import sys
import welcome_text

#global dictionaries
#dictionary containing 1 key. contains a list of numbers that are attack values
meleeSpells = {"Smack": [4, 5, 6, 7]
               
               }
#dictionary that contains 4 keys. Each key contains 4 numbers used for attack values. 
magicSpells = {"Lightning Strike": [2, 3, 4, 5], #Lightning/Electric attack
               "Fireball": [2, 3, 4, 5], #Fire attack
               "Water Cannon": [2, 3, 4, 5], #Water attack
               "Boulder Crush": [2, 3, 4, 5], #Rock/Earth attack
               }

def starting_menu(option):
    '''Is a function that is associated with what you see when you first interact with the game.'''
    while True:
        if option == "Y":
            print("A challenger approaches..")
            return option
        else:
            print("Exiting Gauntlet..")
            return option
        break

def write_file(player): 
    '''A function that writes the player dictionary to an external file, saving the player's name
        the player's starting health, class, and score
    '''
    
    with open('Gauntlet_scores.out', 'a') as fp:
        for k, v in player.items():
            fp.writelines('Player name - {}\nHealth, Class, Score - {}\n\n'.format(k,v))
    return fp     

def swordsman(name, randHealthSword, spellClass, player, score):
    '''Function that assigns all inputs set by the user into the player dictionary.
    Also prints a message if the user has higher or lower generated health.'''

    player[name] = [randHealthSword, spellClass, score] #setting name as key and randomhealth, their spell class, and score as values
    print("Your character's name is " + name + ", your health is "
          + str(randHealthSword) + " and you are a Swordsman.") #print statement that displays info above to user

    if randHealthSword <= 3: #little extra bit if random health is low/high
        print("You look a little frail..")
    elif randHealthSword >= 22:
        print("You feel strong enough to lift a car.")
    return player[name]

def mage(name, randHealthMage, spellClass, player, score):
    '''
    Function that assigns all inputs set by the user into the player dictionary.
    Also prints a message if the user has lower generated health.
    '''

    player[name] = [randHealthMage, spellClass, score] #if the input is in magicSpells dict, assign name as key and random health, spell class, and score as values
    print("Your character's name is " + name + ". Your health is "
          + str(randHealthMage) + " and you are a Mage.")

    if randHealthMage <= 3: #little extra bit if random health is low/high
        print("You look a little frail..")
    return player[name]

def monsters(randChoice, strength):
    '''
    Gives monsters a type, weakness, and attack/health
    There are five monsters and each get their own dictionary
    
    randChoice is a variable that is run in the combat loop, gives a random choice of monster to the user
    
    type: type of monster
    
    Weakness: what spells the monster is weak to
    
    attack: how strong the monster is plus how much stronger they get with each round
    
    health: same as attack
    ''' 
    if randChoice == 1:
        troll = {'type': "Troll", "Weakness": "None", 'attack': strength*3+3, 'health': strength*3+3}	#No weakness!
        return troll
    elif randChoice == 2: 
        skeleton_soldier = {'type': "Skeleton Soldier", 'Weakness': "Rock", 'attack': strength*2+2, 'health': strength*3+3} #weak to rock
        return skeleton_soldier
    elif randChoice == 3:
        treant = {'type': "Treant", 'Weakness': "Fire", 'attack': strength*1+1, 'health': strength*4+4}  #weak to fire
        return treant
    elif randChoice == 4:
        flame_imp = {'type': "Flame Imp", 'Weakness': "Water", 'attack': strength*4+4, 'health': strength*1+1}  #weak to water
        return flame_imp
    elif randChoice == 5:
        water_elemental = {'type': "Water Elemental", 'Weakness': "Lightning", 'attack': strength*3+3, 'health': strength*2+2}  #weak to lightning
        return water_elemental


def combatMage(player, name, monster):
    '''
    Handles combat for Mage classs
    imports the magicSpells global dictionary
    Uses: player dictionary,
           key from player dictionary
           monsters function
    '''
    
    global magicSpells
    spellRandom = random.randint(0,3)   #picks damage player will do for the loop from approrpiate dictionary
    playerHealth = player[name][0]      #player health
    monsterHealth = monster['health'] #monster health
    monsterDamage = monster['attack'] #monster's damage
    monsterType = monster['type'] #monster's type
    monsterWeakness = monster['Weakness'] #monster's weakness
    
    print"A ",  monsterType, " with ", monsterHealth, " health and ", monsterDamage, "attack has appeared."
    
    while playerHealth > 0 and monsterHealth > 0:
        x = raw_input("\nSpells: \n\t"
                  "1. Lightning Strike \n\t"
                  "2. Fireball \n\t"
                  "3. Water Cannon \n\t"
                  "4. Boulder Crush\n"
                  "Input your choice: ") #X is the spell being cast
        if x == '1':
            playerDamage = magicSpells['Lightning Strike'][spellRandom]     #Deals random damage from magicSpells
            if monsterWeakness == "Lightning":
                monsterHealth = monsterHealth - (2*playerDamage) #the amount of damage the player deals is subtracted from the monster's health
                                                                 #double damage is dealt is monster is weak to certain type of spell
                print "You did ", 2*playerDamage, "damage (Double Damage!)" #make monster lose twice as much health

                if monsterHealth < 0:
                    monsterHealth = 0
            
            else:
                monsterHealth = monsterHealth - playerDamage        #deals nomral damage. 

                if monsterHealth < 0:           #monster's health won't go below 0
                    monsterHealth =0
                print "You did ", playerDamage, "damage!"
            print "The ", monsterType," has ", monsterHealth, " health left!"

        elif x == '2': 
            playerDamage = magicSpells['Fireball'][spellRandom]         #Deals random damage from magicSpells
            if monsterWeakness == "Fire":
                
                monsterHealth = monsterHealth - (2*playerDamage)
                print "You did ", 2*playerDamage, "damage (Double Damage!)" #make monster lose twice as much health

                if monsterHealth < 0:
                    monsterHealth =0
            
            else:
                monsterHealth = monsterHealth - playerDamage

                if monsterHealth < 0:           #monster's health won't go below 0
                    monsterHealth =0
                print "You did ", playerDamage, "damage!"
            print "the ", monsterType," has ", monsterHealth, " health left!"
        elif x == '3':
            playerDamage = magicSpells['Water Cannon'][spellRandom]         #Deals random damage from magicSpells
            if monsterWeakness == "Water":
                monsterHealth = monsterHealth - (2*playerDamage)
                print "You did ", 2*playerDamage, "damage (super effective!)" #make monster lose twice as much health

                if monsterHealth < 0:
                    monsterHealth =0
            
            else:
                monsterHealth = monsterHealth - playerDamage

                if monsterHealth < 0:           #monster's health won't go below 0
                    monsterHealth =0
                print "You did ", playerDamage, "damage!"
            print "the ", monsterType," has ", monsterHealth, " health left!"
        elif x == '4':
            playerDamage = magicSpells['Boulder Crush'][spellRandom]        #Deals random damage from magicSpells
            if monsterWeakness == "Rock":
                monsterHealth = monsterHealth - (2*playerDamage)
                print "You did ", 2*playerDamage, "damage (super effective!)" #make monster lose twice as much health

                if monsterHealth < 0:
                    monsterHealth =0
            
            else:
                monsterHealth = monsterHealth - playerDamage

                if monsterHealth < 0:           #monster's health won't go below 0
                    monsterHealth =0
                print "You did ", playerDamage, "damage!"
            print "the ", monsterType," has ", monsterHealth, " health left!"
        else:
            print("You did nothing.")
        #Damage calculation for player. Monster can't attack if it dies previously
        if monsterHealth > 0:
            playerHealth = playerHealth - monsterDamage
            if playerHealth < 0:
                playerHealth = 0    
            print "You were struck by the ", monsterType," for ", monsterDamage," and have ", playerHealth," health left."
    return playerHealth

def combatSwordsman(player, name, monster):
    '''
    Handles combat for Swordsman classs
    imports the meleeSpells global dictionary
    Uses: player dictionary,
           key from player dictionary
           monsters function
    '''
    
    global meleeSpells

    playerHealth = player[name][0]          #player health
    monsterHealth = monster['health'] #monster health
    monsterDamage = monster['attack'] #monster's damage
    monsterType = monster['type'] #
    print "A ",  monsterType, " with ", monsterHealth, " health and ", monsterDamage, "attack has appeared." 
    while playerHealth > 0 and monsterHealth > 0:
        x = raw_input("\nMoves: \n\t" #only two moves because Swordsmen are inherently dumb
                  "1. Smack \n\t"
                  "2. Get Smacked \n\t"
                  "Input your choice: ") #X is the spell being cast
        if x == '1':
            playerDamage = meleeSpells['Smack'][random.randint(0,3)]        #Random damage from meleeSpells
            monsterHealth = monsterHealth - playerDamage #the amount of damage the player deals is subtracted from the monster's health
            if monsterHealth < 0:       #makes sure monster's health doesn't go below 0
                monsterHealth =0
            print "You did ", playerDamage, "damage!"
            print "the ", monsterType," has ", monsterHealth, " health left!"

        elif x == '2': 
            print "For some reason, you decided to \"Get Smacked\" "
        
        else:
            print("You did nothing.")
        if monsterHealth > 0:		#If statement makes sure that you don't take damage if the monster dies
            playerHealth = playerHealth - monsterDamage
            if playerHealth < 0:
                playerHealth = 0    
            print "You were struck by the ", monsterType," for ", monsterDamage," and have ", playerHealth," health left."
    return playerHealth

def upgradeMage():          #EDITS DICTIONARY TO UPGRADE ABILITIES
    '''Function that upgrades the list of numbers within the mageSpells dictionary'''
    
    magicSpells['Lightning Strike'] = [i + 2 for i in magicSpells['Lightning Strike']]  #INCREASES DAMAGE OF LIGHTNING STRIKE
    magicSpells['Fireball'] = [i + 2 for i in magicSpells['Fireball']]          #INCREASES DAMAGE OF FIREBALL
    magicSpells['Water Cannon'] = [i + 2 for i in magicSpells['Water Cannon']]      #INCREASES DAMAGE OF WATER CANNON
    magicSpells['Boulder Crush'] = [i + 2 for i in magicSpells['Boulder Crush']]   #INCREASES DAMAGE OF BOULDER CRUSH

def upgradeSwordsman():     #EDITS DICTIONARY TO UPGRADE ABILITIES
    '''Function that upgrades the list of numbers within the meleeSpells dictionary'''
    
    meleeSpells['Smack'] = [i + 3 for i in meleeSpells['Smack']]

def main():
    '''
    Main function that runs every function from above. Contains multiple while loops for:
    starting the game, character customization, upgrades, writing to file
    '''
    player = {} #setting player as an empty dict so the while loop can add to it
    randHealthSword = random.randint(1,25) #randomly setting health for melee players
    randHealthMage = random.randint(1,15) #randomly setting health for mage players
    score = 0 #set as 0, to be updated when user defeats monsters
    spellClass = '' #empty string until it is called, is stored into player dictionary
    name = '' #empty string, to be used as a key for the player dictionary 

    welcome_text.welcome_text() #beginning print, calls the utility file welcome_text
    option = raw_input("Would you like to play? Y/N - ").upper()

    starting_menu(option) #takes option
    if option == 'Y':
        name = raw_input("What is your name? ").title() #ask user for desired name of character
        print("Hello, " + name + ".")

        while True: 
            spellClass = raw_input("Swordsman or Mage? ").upper() #asks user if they want to be swordsman/mage 
            print("\n")

            if spellClass == 'SWORDSMAN':
                swordsman(name, randHealthSword, spellClass, player, score) #calls swordsman function is user chooses to be a swordsman                
                break
            elif spellClass == 'MAGE':
                mage(name, randHealthMage, spellClass, player, score) #calls mage function is user chooses to be a swordsman           
                break
            else:
                print("That isn't a listed type!") #message appears when user inputs something that isn't swordsman or mage
    else:
        print("Can't you smell the circus, Georgie? There's peanuts... cotton candy... hot dogs... and...") #exit the program
        sys.exit(0)


    maxHealth = player[name][0] #calling player dictionary at index 0 returns health
    playerHealth = maxHealth 
    
    while playerHealth > 0 and spellClass == 'MAGE':            #runs combat if you are a mage
        randChoice = random.randint(1,5) #random choice between 1 and 5
        monster = monsters(randChoice, score) #the number from randChoice is used in this monster function to call a random monster
        playerHealth = combatMage(player, name, monster) #put arguments
        score += 1 
        
        if playerHealth <= 0: #if player dies, run this if
            print("You died. Get better, you scrub. \n")
            print("Here lies " + name + " the Mage. " 
                  + name + " killed " + str(score) + " monsters.")
            player[name][2] = score #score gets assigned to index #2 in dict
            write_file(player) #calls write_file function
            break
        else:
            upgrade = raw_input("\nWould you like to: \n\t\n" #else, lets the player upgrade
                            "\t1. Restore your health \n\t"
                            "2. Upgrade your spells \n\t\n"
                            "Or input anything else to do nothing.\n"
                            "Input your choice: ")
        if upgrade == '1':
            playerHealth = maxHealth
            print("Your health has been restored!") #restore health
        elif upgrade == '2':
            print ("Your knowledge of magic grows!") #calls the upgradeMage function
            upgradeMage()    
        else:
            print("Playing on hard mode, I see. Good luck.") #if you input nothing, this appears and continues to the next combat loop
        
        print "Your current score is: ", score
        player[name][0] = playerHealth
        
    while playerHealth > 0 and spellClass == 'SWORDSMAN':           #Runs if combat if you are a swordsman
        randChoice = random.randint(1,5) #random choice between 1 and 5
        monster = monsters(randChoice, score) #the number from randChoice is used in this monster function to call a random monster
        
        playerHealth = combatSwordsman(player, name, monster) 
        
        if playerHealth <= 0:
            print("You died. Get better, you scrub. \n") #same function as the one above
            print("Here lies " + name + " the Swordsman. " 
                  + name + " killed " 
                  + str(score) + " monsters. ") 
            player[name][2] = score
            write_file(player)
            break
        else:
            upgrade = raw_input("\nWould you like to: \n\t\n"	#lets the player decide to restore their health or improve the damage from their sword
                            "\t1. Restore your health \n\t"
                            "2. Upgrade your sword \n\t\n"
                            "Or input anything else to do nothing.\n"
                            "Input your choice: ")
        if upgrade == '1':
            playerHealth = maxHealth
            print("Your health has been restored!")
        elif upgrade == '2':
            upgradeSwordsman()					#runs upgrade function for swordsman
            print ("You have a bigger, shinier, pointier sword! :O")
        else:
            print("Playing on hard mode, I see. Good luck.")
        player[name][0] = playerHealth
        score += 1   
        print "Your current score is: ", score    
main()
