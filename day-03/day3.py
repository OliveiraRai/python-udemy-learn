### CONTROL FLOW AND LOGICAL OPERATORS
# if condition:
#     do this (if condition is true)
# else:
#     do this (if condition is false)


# print("Welcome to the Odd or Even Identifier program!")
# number = int(input("Choose an integer number: "))
# if number % 2 == 0:
#     print(f"{number} is Even.")
# else:
#     print(f"{number} is Odd.")

# print("Welcome to the rollercoaster!")
# height = int(input("How much do you height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("How old are you? "))
#     if age < 12:
#         print("You may pay $5 for the ticket!")
#         bill += 5
#     elif age <= 18:
#         print("You may pay $7 for the ticket!")
#         bill += 7
#     elif age >= 45 and age <= 55:
#         print("You may enter for free!")
#         bill += 0
#     else:
#         print("You may pay $12 for the ticket!")
#         bill += 12
#     want_photo = input("Do you want photos? y/n :")
#     if want_photo == "y":
#         bill += 3
    
#     print(f"The total bill is ${bill}")
# else:
#     print("You can't ride the rollercoaster...")

# print("Welcome to the BMI Calculator!")
# height = float(input("How much do you height? Example: 1.80\n"))
# weight = float(input("How much do you weight? Example: 70.5\n"))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print(f"BMI equals {bmi:.1f}. You're underweighted!")
# elif bmi < 25:
#     print(f"BMI equals {bmi:.1f}. You're at your normal weight!")
# else: 
#     print(f"BMI equals {bmi:.1f}. You're overweighted!")

# print("Welcome to the Python Pizzaria!")
# bill = 0
# size = input("What size pizza do you want? S, M or L: ")
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("Please, insert a valid value.")
# pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
# if pepperoni == "y" and size == "S":
#     bill += 2
# elif pepperoni == "y" and (size == "M" or "L"):
#     bill += 3
# extra_cheese = input("Do you want extra cheese? y or n: ")
# if extra_cheese == "y":
#     bill += 1
# print(f"Your final bill is ${bill}")

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