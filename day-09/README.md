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

_Nesting_
É o ato de *agrupar* listas ou dicionários dentro de dicionários.
# nested = {
#   "a_list" = ["value1", "value2", ..., "valueN"],
#   "a_dict" = {
#       "key1": "value",
#       "key2": ["value"]
#   }
# }

Para chamar printar 'value2', fazemos:
# print(nested["a_list"][1])

Para chamar 'value' em key2, fazemos:
# print(nested["a_dict"]["key2"][0])

*Como se entrássemos em pastas e subpastas, usando aspas para dicionários e índices para listas*

_IMPORTANTE_
Em dicionários, podemos apenas acessar os valores da chaves usando as chaves, mas não podemos -
nativamente - buscar a chave pelo seu valor.

