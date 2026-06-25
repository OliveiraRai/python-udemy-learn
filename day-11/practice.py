import random

lista = [1,2,3,4,5]
pegar_1_item = random.choice(lista)
print(f"Um item apenas: {pegar_1_item}") # retorna 1 item apenas

pegar_mais_de_um = random.sample(lista, 2)
print(f"Mais de um item: {pegar_mais_de_um}") # Retorna 2 itens