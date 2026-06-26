import random

# lista = [1,2,3,4,5]
# pegar_1_item = random.choice(lista)
# print(f"Um item apenas: {pegar_1_item}") # retorna 1 item apenas

# pegar_mais_de_um = random.sample(lista, 2)
# print(f"Mais de um item: {pegar_mais_de_um}") # Retorna 2 itens

# hand1, hand2 = [], []
# print(hand2)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def verify_ace(hand, score):
    if hand[-1] == 11 and score > 21:
        hand[-1] = 1
        score = sum(hand)

def p_start_cards(hand, score):
    hand = random.sample(cards, 2)
    score = sum(hand)
    verify_ace(hand, score)
    return hand, score
    
def pseudo_blackjack():
    p_hand, p_score = [], 0
    p_hand, p_score = p_start_cards(p_hand, p_score)
    print(p_hand, p_score)
    
pseudo_blackjack()