Dia do grande projeto python: Blackjack, e sua lógica.

Aprendizados ao longo do 'caminho':
- função built-in *sample()*, que tem o poder de retornar mais de 1 item de uma lista.
    - existe mais nessa função do que descrevi; _Ler mais sobre_.
- a função built-in *sum()* tem o poder de somar todos os itens numa lista.
- criação de funções para blocos de códigos que se repetem
- não é mais usado função recursiva, e sim, uma função menu com loop
    - ao usar funções recursivas, o último estado da função é guardado. O que pode
      acontecer - em algum momento - retornar RecursionError.
        - o Python verifica até 1000 chamadas recursivas, depois retorna erro.
- *uso de 'r'* antes de _docstrings_ para tratar o conteúdo da string literalmente, sem caracteres escape (como a barra invertida '\' e a quebra de linha \n)

no final, aprendi sobre como melhor separar cada block de código com sua funcionalidade única. Assim, uma função guarda a lógica do programa; outras função guardam sub-lógicas do programa para serem chamadas na função principal; e outra função para servir como iterador de lógica sem
ter que usar múltiplos while's no mesmo bloco ou inúmeras funções recursivas.

Resumindo, estou aprendendo a tornar o código final mais eficiente e legível.