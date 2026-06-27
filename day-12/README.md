O desafio deste dia é o jogo Guess the Number. 

### Lógica
Onde a máquina ira escolher um numéro aleatório dentro de um range, e o jogador terá x palpites (de acordo com dificuldade). A cada erro, a maquina diz se o palpite do jogador está baixo ou alto em relação ao número da vez. Ao descobrir o número, você vence.

### Passos (not in order, problably)
- uso da função built-in random: *choice()*
- *variáveis* que vão guardar o número escolhido pela máquina, pelo jogador e número de vidas.
- _inputs para escolher dificuldade_, ou seja, *mais uma variável* para guardar a dificuldade.
- função *verify_guess()* para verificar se o palpite do jogador está alto ou baixo e retornar string de acordo.
- assim como o dia anterior, é bom usar uma função *menu()* para cuidar do loop
- uma função *guess_number()* que guardará a lógica inteira do jogo. 
- uso de *arte em ascii* para personalidade e vida.
    