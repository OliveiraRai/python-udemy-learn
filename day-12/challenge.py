import random

EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5

def setAttempts():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        attempts = 0
        if difficulty == 'easy':
            return EASY_DIFFICULTY_ATTEMPTS
        elif difficulty == 'hard':
            return HARD_DIFFICULTY_ATTEMPTS
        else:
            print("  Please, choose a valid difficulty.\n")

def setNumber():
    number = random.choice(range(1, 101))
    return number

def guess_the_number():
    attempts = setAttempts()
    number = setNumber()
    print(f"You have {attempts} attempts remaining to guess the number.")
    while True:
        if attempts == 0:
            print("  You have run out of guesses. You lose.\n") 
            break
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            break
        elif guess > number:
            attempts -= 1
            print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
        elif guess < number:
            attempts -= 1
            print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")       
    
def menu():
    while True:
        choice = input("Do you want to play a round of Guess The Number? Type 'yes' or 'no': ").lower()
        if choice == 'yes':
            print("\n" * 20)
            logo = r"""  ________                            ___________.__            _______               ___.                 
 /  _____/ __ __   ____   ______ _____\__    ___/|  |__   ____  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |    |   |  |  \_/ __ \ /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  |    |   |   Y  \  ___//    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > |____|   |___|  /\___  >____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                \/     \/        \/            \/    \/     \/       """
            print(logo)
            print("Welcome to the Number Guessing Game!")
            print("I'm thinking of a number between 1 and 100.")
            guess_the_number()
        elif choice == 'no':
            print("  Come back anytime!")
            break
        else:
            print("  Please, write a valid answer. (yes/no)\n")
                     
menu()