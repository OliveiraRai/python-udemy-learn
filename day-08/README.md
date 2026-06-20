Aprendizado em uso de parametros em funções. 

Desafio consiste em construir a lógica da Cifra de César, onde eu consegui fazer; embora haja bugs para corrigir, como:

- shift number pode estourar a quantidade de letras de a-Z
    - Retornando *IndexError: list index out of range*
- validação

Outros aprendizados:

- Uso do módulo *str()* que transforma o que não é string, em string 
    - Para transformar lista em string, usa-se *join()*
        - Este módulo funciona da seguinte maneira:
            minha_lista = ["Hello", "World"]
            mensagem = " ".join(minha_lista)
            print(mensagem) # retorna "Hello World"
            # onde o que estiver dentro de parênteses será usado como separador dos índices
            # Se fosse ",".join(minha_lista) retornaria Hello,World
- *Positional argument* vs *Keyword argument*
- Uso do módulo *index()* para encontrar o index em uma lista do qual você já tem o valor existente "em mãos"
- Blocos Try-Except para tratar erros sem acabar com o fluxo do programa.
- Uso do módulo type() para tratar e validar dados.
- Uso do operador módulo (%) para criar ciclos infinitos (efeito "relógio"):
    - Este operador retorna o resto da divisão inteira entre dois números.

    - Quando aplicado ao tamanho de uma lista (como o alfabeto de 26 letras), ele garante que qualquer número — por maior que seja — dê a volta e retorne um índice válido entre 0 e 25.
    Python

    # Exemplo prático:
    novo_indice = (indice_atual + shift_number) % 26

    - Se a soma for menor que 26, o número permanece igual. Se passar de 26, o módulo calcula automaticamente "quantas letras passaram" e recomeça do início, eliminando o erro de IndexError sem precisar de if/else.
