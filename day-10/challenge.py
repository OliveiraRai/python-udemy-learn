def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# times = operations["*"]
# print(times(4, 8)) # Esse foi o que eu fiz
# print(operations["*"](4, 8)) # Esse foi o que a professora fez. Bem melhor.
# Eu podia ter feito o que eu pensei nas linhas 20-23 do arquivo practice.py
# operations["*"] pode ser lido também como 'add' apenas.
# em linha, ficaria:
# add
# e para chamar a função em si, faríamos:
# add()
# ou seja, 'operations["*"]()' faz sentido. Só me resta entender a ponto de enxergar mais.

print("Welcome to the best calculator out there.")
while True:
    will_continue = "y"
    while True:
        try:
            n1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please, enter a valid number.")
            print("")
    while will_continue == "y":
        while True:
            operator_choice = input("Choose one between the four operations:\n  +\n  -\n  *\n  /\nChoice: ")
            if operator_choice not in operations:
                print("Please, enter a valid operation.")
                print("")
                continue
            else:
                break
        while True:
            try:
                n2 = int(input("Enter another number: "))
                break
            except ValueError:
                print("Please, enter a valid number.")
                print("")
        if n2 == 0: # Isso virou uma validação sem querer haha
            print(f"The calculation between {n1} and 0 is undefined.")
            continue
        if operator_choice == "+":
            print(f"{n1} {operator_choice} {n2} = {operations["+"](n1, n2)}")
            n1 = operations["+"](n1, n2)
        elif operator_choice == "-":
            print(f"{n1} {operator_choice} {n2} = {operations["-"](n1, n2)}")
            n1 = operations["-"](n1, n2)
        elif operator_choice == "*":
            print(f"{n1} {operator_choice} {n2} = {operations["*"](n1, n2)}")
            n1 = operations["*"](n1, n2)
        elif operator_choice == "/":
            print(f"{n1} {operator_choice} {n2} = {operations["/"](n1, n2)}")
            n1 = operations["/"](n1, n2)
        else:
            print("Please, choose a valid option.")
        will_continue = input("If you want to continue with this result, type 'y'. If you want to start a new calculation, type 'n'.\n  ")