*Aprendendo a como usar dicionários e nesting.*

Dicionário são como listas, embora funcionem com chave e valor. Da seguinte forma:
# meu_dicionario = {chave: valor}

Quando há mais de uma chave, faz:
# meu_dicionario = {
#     chave1: valor,
#     chave2: valor,
#     ...
#     chaveN: valor
# }

Em chave, devemos se atentar ao erro *KeyError* - onde o valor chamado de chave não existe
dentro do dicionário. *Cuidado também ao colocar um valor string sem aspas*, pois - ao rodar - 
pode retornar erro por esperar existir um variável anteriormente. 
# NameError: name 'nome da chave' is not defined

*Dicionário vázios - assim como listas - podem ser criados* da seguinte forma:
# meu_dicionario = {}

Pode ser populado 
# meu_dicionario[chave] = valor

Um *dicionário já populado pode ser fácilmente limpado* usando o código da linha 20, colocado
posteriormente a um dicionário populado. e.g. retorna apenas "{}"

Pode-se *mudar também o valor de uma chave já existente* usando o código da linha 23, onde {chave} é uma chave existente no dicionário.


