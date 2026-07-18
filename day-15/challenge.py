MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# pegar input
choice = input("What would you like? (espresso/latte/cappuccino):")

# ver se temos recursos necessários para fazer a operação
for ingredient in MENU[choice]["ingredients"]:
    if (MENU[choice]["ingredients"][ingredient]) > resources[ingredient]:
        print("Sorry, there is not enough ingredients")
        break

# cobrar
print("Please, insert coins.")
quarter = int(input("How many quarters? "))
dime = int(input("How many dimes? "))
nickle = int(input("How many nickles? "))
penny = int(input("How many nickles? "))

# verificar se pagamento é maior ou igual ao preço > se sim, aceitar e prosseguir > se não, recusar e retornar o dinheiro
