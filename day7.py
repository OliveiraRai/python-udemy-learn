import random

### Hangman challenge
word_list = ["cat", "dog", "sun", "book", "tree", "apple", "fish", "ball", "blue", "jump"]
chosen_word = random.choice(word_list)
# list() here transforms string into a list dividing it by characters
word = list(chosen_word)
blank = "_"
list_of_blanks = [blank for letters in chosen_word]

guess = ""
letters_guessed = []
isWord_guessed = False

life = 6

# isalpha() checks if variable value is a "a-Z" range 
while isWord_guessed == False:
    print(f"Life: {life}")
    print(f"Letters guessed: {letters_guessed}")
    print(list_of_blanks)
    # isalpha verifies if variable is a letter or not
    while not guess.isalpha():
        # lower() changes uppercase to lowercase
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha():
            print("Please, choose a letter.")
            print()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            list_of_blanks[index] = guess
    
    # "if x in y" is something I would never think of by myself lol 
    if guess not in word:
        life -= 1

    if life == 0:
        print("The poor guy was hanged up because of your imcompetence :(")
        break

    count = 0
    for x in list_of_blanks:
        if x == blank:
            count += 1

    if count == 0:
        print(f"You've guessed it! it was {chosen_word}.")
        isWord_guessed = True

    letters_guessed.append(guess)
    guess = ""