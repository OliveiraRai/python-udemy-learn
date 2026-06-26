import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def verify_ace(hand, score):
    while 11 in hand and score > 21:
        ace_index = hand.index(11)
        hand[ace_index] = 1
        score = sum(hand)
    return hand, score

def p_start_cards(hand, score):
    hand = random.sample(cards, 2)
    score = sum(hand)
    hand, score = verify_ace(hand, score)
    return hand, score
        
def c_start_cards(hand, score):
    hand = random.sample(cards, 2)
    score = sum(hand)
    hand, score = verify_ace(hand, score)
    return hand, score
        
def give_cards(hand, score):
    hand.append(random.choice(cards))
    score = sum(hand)
    hand, score = verify_ace(hand, score)
    return hand, score

def blackjack():
    p_hand, c_hand, p_score, c_score = [], [], 0, 0
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
    p_hand, p_score = p_start_cards(p_hand, p_score)
    c_hand, c_score = c_start_cards(c_hand, c_score)
    print(f"  Your cards: {p_hand}, current score: {p_score}")
    print(f"  Computer's first card: {c_hand[0]}")
    while True:
        wanna_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if wanna_continue == 'n':
            while c_score < 17:
                c_hand, c_score = give_cards(c_hand, c_score)
            print(f"  Your final hand: {p_hand}, final score: {p_score}")
            print(f"  Computer's final hand: {c_hand}, final score: {c_score}")
            if p_score == 21 and len(p_hand) == 2 and c_score == 21 and len(c_hand) == 2:
                print("Draw! Both you and the opponent have a Blackjack.")
                break
            elif len(p_hand) == 2 and p_score == 21:
                print("Win with a Blackjack!")
                break
            elif len(c_hand) == 2 and c_score == 21:
                print("Opponent wins with a Blackjack.")
                break
            elif c_score > 21:
                print("Opponent went over. You win.")
                break
            elif p_score > c_score:
                print("You win.")
                break
            elif c_score > p_score:
                print("You lose.")
                break
            else:
                print("Draw")
                break
        elif wanna_continue == 'y':
            p_hand, p_score = give_cards(p_hand, p_score)
            print(f"  Your cards: {p_hand}, current score: {p_score}")
            print(f"  Computer's first card: {c_hand[0]}")
            if p_score > 21:
                print("You went over. You lose.")
                break
        else: 
            print("Please, choose a valid option.")
    
def menu():
    while True:
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if choice == 'y':
            blackjack()
        elif choice == 'n':
            print("  Come back any time.")
            break
        else:
            print("Please, choose a valid option.")
    
menu()