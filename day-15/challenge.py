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
    "money": 0,
}

COIN_VALUE = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

# pegar input
choice = input("What would you like? (espresso/latte/cappuccino):")

# ver se temos recursos necessários para fazer a operação
for ingredient in MENU[choice]["ingredients"]:
    if (MENU[choice]["ingredients"][ingredient]) > resources[ingredient]:
        print("Sorry, there is not enough ingredients")
        break

# cobrar e dar o troco se necessário
print("Please, insert coins.")
quarter = int(input("How many quarters? "))
dime = int(input("How many dimes? "))
nickle = int(input("How many nickles? "))
penny = int(input("How many nickles? "))
total = (COIN_VALUE["penny"] * penny) + (COIN_VALUE["nickle"] * nickle) + (COIN_VALUE["dime"] * dime) + (COIN_VALUE["quarter"] * quarter)

# verificar se pagamento é maior ou igual ao preço > se sim, aceitar e prosseguir > se não, recusar e retornar o dinheiro
if total >= MENU[choice]["cost"]:
    resources["money"] += total
    if total > MENU[choice]["cost"]:
        change = total - MENU[choice]["cost"]
        resources["money"] - change
        print(f"Here is ${change} in change.")
    print(f"Here is your {choice}. Enjoy!")
else:
    print("what a cheap-ass dude damn")

