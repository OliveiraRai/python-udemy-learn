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

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", 
                     "i", "j", "k", "l", "m", "n", "o", "p", 
                     "q","r", "s", "t", "u", "v", "w", "x", 
                     "y", "z"]

letter = input("fala uma letra ai campeão kk\n  ")
shift = int(input("fala um numero ai paizao kk\n  "))

new_letter = lowercase_letters.index(letter) + shift
if (lowercase_letters.index(letter) + shift) > len(lowercase_letters):
    print(f"a nova letra é {lowercase_letters[new_letter]}")
