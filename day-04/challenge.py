### EXERCIZE
# print("Rock, Paper, Scizor Game!")

# ### machine's move choice
# moves = ["Rock", "Paper", "Scizor"]
# random_number = random.randint(0,2)
# machine_move = moves[random_number]

# ### player's move choice
# player_move = int(input("Please, choose between:\n  1 - Rock\n  2 - Paper\n  3 - Scizor\nChoice: "))
# player_move = player_move - 1

# ### moves comparison
# print(f"You chose {moves[player_move]}!")
# print(f"Machine chose {machine_move}!")

# ### win condition
# # if moves are the same
# if player_move == random_number:
#     print("Draw!")
# # if player choose stone
# elif player_move == 0 and random_number == 2:
#     print("You win!")
# # if player choose paper
# elif player_move == 1 and random_number == 0:
#     print("You win!")
# # if player choose scizor
# elif player_move == 2 and random_number == 1:
#     print("You win!")
# # the remaining situations are losing situations
# else: 
#     print("You lost!")