# def greet():
#     print("Hello Everyone")
#     print("How are you? fine thanks")
#     print("I wish I were a bird")

# greet()

## parameters
# def life_in_weeks(current_age):
#     x = (90 - current_age) * 52
#     print(f"You have {x} weeks left.")
#     ## diabolic challenge pull from the python course
    
# life_in_weeks(56)

## two or more parameters
# def greet_with(name, location):
#     print(f"Hello {name}! How's things going on {location}?")

# greet_with("John", "Alaska") # positional argument
# greet_with(location="Alaska", name="John") # keyword argument

# def calculate_love_score(name1, name2):
#     conc_names = name1.lower() + name2.lower()
#     x = 0
#     y = 0
#     love_score = 0
#     for letter in conc_names:
#         if letter == "t":
#             x += 1
#         if letter == "r":
#             x += 1
#         if letter == "u":
#             x += 1
#         if letter == "e":
#             x += 1
#         if letter == "l":
#             y += 1
#         if letter == "o":
#             y += 1
#         if letter == "v":
#             y += 1
#         if letter == "e":
#             y += 1
            
#     love_score = str(x) + str(y)
#     print(f"Love score: {love_score}")
    
# calculate_love_score("Jessica Brier", "John Ferrier")

### Caesar Cypher
def caesar_cypher():
    print("Welcome to the Caesar Cypher Encoder/Decoder")
    enc_dec = input("Type the option number:\n  1. Encrypt\n  2. Decrypt\nChoice: ")
    message = input("Type your message:\n  ")
    shift_number = input("Type the shift number\n  ")

    if enc_dec == 1:
        print("You chose to enconde.")
    elif enc_dec == 2:
        print("You chose to decode.")
    else:
        print("Please, choose a valid option.")

caesar_cypher()
