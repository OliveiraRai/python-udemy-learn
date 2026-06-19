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

