Este dia teve como tema as funções com saída de dados. Ou seja, aprendemos
a usar *return*

- Usar função built-in *title()*
    - que aparentemente faz o mesmo que *txt.lower().capitalize()*
- Ler *practice.py* nas linhas 20 até 24
- O que são e como usar docstrings
    - """ isso é uma docstring """
        - aparentemente funciona tanto como comentário multi-line quanto como
          uma string multi-line que pode ser atribuída a uma variável.
            - todas as quebras de linhas são mostradas ao print()
- na linha 44 de *challenge.py*, tinha feito *'...not in ("+", "-", ...)'* e, pouco depois,
  questionei se não seria possível apenas usar *operation* no lugar de *(...)* - e acabou que
  eu estava correto!
    - minha lógica era que, ao 'loopear' por *operation* com _for_, ele me retornaria apenas as chaves, ou seja: "+", "-", ...; logo, eu poderia usar apenas a variável ao invés da tupla.
        - lógica está fluindo!!!
- a professora, ao invés do que eu fiz - usar dois while loops - no lugar do primeiro loop, ela
  definiu uma variavel *calculator* e, para que a feature de voltar com n1 'zerado', ela chamou
  a função calculator dentro dela mesma.
    - Isso é chamado de _recursive functions_, onde - para resolver um problema - a função chama
      a si mesma dentro de seu próprio código.
        - O código fica bem mais limpo e faz muito mais sentido.
            - mas vou deixar a minha solução, pois também funciona, mas sei que o método dela
              seria o viável sempre. É mais para visualizar progresso. Sei que o github faz isso,
              mas tenho preguiça de voltar versões de código.