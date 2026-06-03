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