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

def higher_lower():
    person1 = person_picker()
    person2 = verify_duplicity(person1, person_picker())
    print(person1)
    print(person2)
    
higher_lower()