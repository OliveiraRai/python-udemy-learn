# EXERCISE
choice_three = ""
while choice_three == "red" or "blue":
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _ ________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')
    print("Welcome to the Treasure Island!\nYour mission is to find the treasure.")
    choice_one = input("You are at a cross road. Where do you want to go?\n" + "   Type 'right' or 'left'\n" + "Decision: ")
    if choice_one == "left":
        choice_two = input("You have come to a lake! There's an island in the middle of the lake.\n" + "   Type 'swim' to swim across. Type 'wait' to wait for a boat.\n" + "Decision: ")
        if choice_two == "wait":
            choice_three = input("You arrive at the island unharmed! There is a house with 3 doors.\n" + "   One red, one yellow and one blue. Which door do you choose to enter?\n" + "Decision: ")
            if choice_three == "yellow":
                print("You've won! Your prize is the thought that you did it,\nwhich is more valuable than every coin in this world.")
                break
            else:
                print("The door leads you to a familiar place: the beggining of the journey.\nBut somehow you remember your previous try, so try not to make a bad choice.")
        else:
            print("After swimming ahead sometime, your body tries to swim down by itself and you die.")
            break
    else:
        print("You found nothing and you're pretty tired to go back, so you die there.")
        break

## OBS: the loop wasn't part of the exercise, but I thought it would be cool since I added that
##      line on the third choice of the game :)