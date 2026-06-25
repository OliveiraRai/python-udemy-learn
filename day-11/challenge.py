import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        print("\n" * 20)
        blackjack_art = r"""
         _     _            _    _            _    
        | |   | |          | |  (_)          | |   
        | |__ | | __ _  ___| | ___  __ _  ___| | __
        | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        | |_) | | (_| | (__|   <| | (_| | (__|   < 
        |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                               _/ |                
                              |__/ 
        """
        print(blackjack_art)
        p_hand = random.sample(cards, 2)
        c_hand = random.sample(cards, 2)
        p_score = sum(p_hand)
        c_score = sum(c_hand)
        print(f"  Your cards: {p_hand}, current score: {p_score}")
        print(f"  Computer's first card: {c_hand[0]}")
        while True:
            wanna_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if wanna_continue == 'n':
                while c_score < 17:
                    c_hand.append(random.choice(cards))
                    c_score = sum(c_hand)
                    if c_hand[-1] == 11 and c_score > 21:
                        c_hand[-1] = 1
                        c_score = sum(c_hand)
                print(f"  Your final hand: {p_hand}, final score: {p_score}")
                print(f"  Computer's final hand: {c_hand}, final score: {c_score}")
                if c_score > 21:
                    print("Opponent went over. You win.")
                    blackjack()
                elif len(p_hand) == 2 and p_score == 21:
                    print("Win with a Blackjack")
                    blackjack()
                elif (len(c_hand) == 2 and c_score == 21):
                    print("Oponent wins with a Blackjack")
                    blackjack()
                elif p_score > c_score:
                    print("You win.")
                    blackjack()
                elif c_score > p_score:
                    print("You lose.")
                    blackjack()
                else:
                    print("Draw")
                    blackjack()
            elif wanna_continue == 'y':
                p_hand.append(random.choice(cards))
                p_score = sum(p_hand)
                if p_hand[-1] == 11 and p_score > 21:
                    p_hand[-1] = 1
                    p_score = sum(p_hand)
                print(f"  Your cards: {p_hand}, current score: {p_score}")
                print(f"  Computer's first card: {c_hand[0]}")
                if p_score > 21:
                    print("You went over. You lose.")
                    blackjack()
            else: 
                print("Please, choose a valid option.")
    elif choice == 'n':
        print("  Come back any time.")
    else: 
        print("Please, choose a valid option.")
        blackjack()
    
blackjack()