### Caesar Cypher
def caesar_cypher():
    lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", 
                         "i", "j", "k", "l", "m", "n", "o", "p", 
                         "q","r", "s", "t", "u", "v", "w", "x", 
                         "y", "z"]
    capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", 
                       "I", "J", "K", "L", "M", "N", "O", "P", 
                       "Q", "R", "S", "T", "U", "V", "W", "X", 
                       "Y", "Z"]

    print("Welcome to the Caesar Cypher Encoder/Decoder")
    while True:
        try:
            enc_dec = int(input("Type the option number:\n  1. Encrypt\n  2. Decrypt\nChoice: "))
            if type(enc_dec) == int:
                break
        except ValueError as error:
            print(f"Invalid option: {error}.")
            print()
    message = input("Type your message:\n  ")
    shift_number = int(input("Type the shift number\n  "))

    if enc_dec == 1:
        enc_message = list(message)

        for index, letter in enumerate(enc_message):
            if letter.isalpha() and letter in lowercase_letters:
                new_letter = (lowercase_letters.index(f'{letter}') + shift_number) % 26
                enc_message[index] = lowercase_letters[new_letter]
            if letter.isalpha() and letter in capital_letters:
              new_letter = (capital_letters.index(f'{letter}') + shift_number) % 26
              enc_message[index] = capital_letters[new_letter]
        print(f"The encoded message will be: {"".join(enc_message)}")
        
    elif enc_dec == 2:
        dec_message = list(message)

        for index, letter in enumerate(dec_message):
            if letter.isalpha() and letter in lowercase_letters:
                new_letter = (lowercase_letters.index(f'{letter}') - shift_number) % 26
                dec_message[index] = lowercase_letters[new_letter]
            if letter.isalpha() and letter in capital_letters:
                new_letter = (capital_letters.index(f'{letter}') - shift_number) % 26
                dec_message[index] = capital_letters[new_letter]
        print(f"The decoded message will be: {"".join(dec_message)}")
    else:
        print("Please, choose a valid option.")

caesar_cypher()

## precisa melhorar 
## - validação (Feito)
## - correção de bug (listar estourar por shift number alto) (feito)
##      - fazer uso do módulo % de um jeito nunca visto antes pela humanidade
## - alfabetos devem ser separados em duas listas, sendo uma para maiúsculas e outra para
##   minúsculas (feito)
##   - ou seja, a lógica do shift number deve ser refeita
