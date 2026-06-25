import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
wanna_play = False
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if choice == 'y':
    wanna_play = True
while wanna_play == True:
    p_hand = random.sample(cards, 2)
    c_hand = random.sample(cards, 2)
    p_score = sum(p_hand)
    c_score = sum(c_hand)
    print(f"  Your cards: {p_hand}, current score: {p_score}")
    print(f"  Computer's first card: {c_hand[0]}")
    wanna_continue = input("Type 'y' to get another card, type 'n' to pass: ")
    if wanna_continue == 'y':
        p_hand.append(random.choice(cards))
        p_score = sum(p_hand)
        print(f"  Your cards: {p_hand}, current score: {p_score}")
        print(f"  Computer's first card: {c_hand[0]}")
        if p_score > 21:
            print("You went over. You lose.")
            choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            continue
    elif wanna_continue == 'n':
        print("conta ota kk")
    else:
        print("Please, choose a valid option.")
    wanna_play = False