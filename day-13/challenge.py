import random

GAME_DATA = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 673,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 512,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 414,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 390,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 390,
        "description": "Actor and former professional wrestler",
        "country": "United States"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 371,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 352,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Beyoncé",
        "follower_count": 307,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 292,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 275,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Neymar",
        "follower_count": 234,
        "description": "Footballer",
        "country": "Brazil"
    },
    {
        "name": "Zendaya",
        "follower_count": 176,
        "description": "Actress and singer",
        "country": "United States"
    }
]

def person_picker():
    person = random.choice(GAME_DATA)
    return person

def verify_duplicity(person1, person2):
    while person1 == person2:
        person2 = person_picker()
    return person2

def higher_lower(logo, vs):
    game_score = 0
    person1 = person_picker()
    print(logo)
    while True:
        person2 = verify_duplicity(person1, person_picker())
        print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}")
        print(vs)
        print(f"Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower() 
        while guess == "":
            print("\n  Your guess cannot be blank.")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower() 
        if person1["follower_count"] > person2["follower_count"] and guess == 'a':
            game_score += 1
            print('/n' * 20)
            print(logo)
            print(f"  You're right! Current score: {game_score}")
            continue
        elif person2["follower_count"] > person1["follower_count"] and guess == 'b':
            game_score += 1
            print('/n' * 20)
            print(logo)
            print(f"  You're right! Current score: {game_score}")
            continue
        else:
            print("\n" * 20)
            print(logo)
            print(f"  Sorry, that's wrong. Final score: {game_score}")
            break
        
def menu():
    logo = r"""  _  _ _      _            
 | || (_)__ _| |_  ___ _ _ 
 | __ | / _` | ' \/ -_) '_|
 |_||_|_\__, |_||_\___|_|  
 | |   _|___/__ _____ _ _  
 | |__/ _ \ V  V / -_) '_| 
 |____\___/\_/\_/\___|_|   
                           """
    vs = r""" __   __    
 \ \ / /__  
  \ V (_-<_ 
   \_//__(_)
            """
    while True:
        choice = input("Do you want to play a round of Higher Lower? Type 'yes' or 'no': ").lower()
        if choice == 'yes':
            print("\n" * 20)
            higher_lower(logo, vs)
        elif choice == 'no':
            print("\n  Come back anytime!")
            break
        else:
            print("\n  Please, write a valid option.")
        
menu()