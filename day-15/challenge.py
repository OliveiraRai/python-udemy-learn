MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}

COIN_VALUE = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

def CoffeeMachine():
    while True:
        hasIngredients = True

        # pegar input
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        # adiciona report (escondido)
        if choice == "report":
            for resource in resources:
                if resource == "Water":
                    print(f"{resource}: {resources[resource]}ml")
                elif resource == "Milk":
                    print(f"{resource}: {resources[resource]}ml")
                elif resource == "Coffee":
                    print(f"{resource}: {resources[resource]}g")
                else:
                    print(f"{resource}: ${resources[resource]}")
            continue

        # ver se temos recursos necessários para fazer a operação
        for ingredient in MENU[choice]["ingredients"]:
            if (MENU[choice]["ingredients"][ingredient]) > resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}")
                hasIngredients = False
                break
        
        if hasIngredients == False:
            continue

        # cobrar e dar o troco se necessário
        print("Please, insert coins.")
        quarter = int(input("How many quarters? "))
        dime = int(input("How many dimes? "))
        nickle = int(input("How many nickles? "))
        penny = int(input("How many nickles? "))
        total = (COIN_VALUE["penny"] * penny) + (COIN_VALUE["nickle"] * nickle) + (COIN_VALUE["dime"] * dime) + (COIN_VALUE["quarter"] * quarter)

        # verificar se pagamento é maior ou igual ao preço > se sim, aceitar e prosseguir > se não, recusar e retornar o dinheiro
        if total >= MENU[choice]["cost"]:
            for ingredient in MENU[choice]["ingredients"]:
                for resource in resources:
                    if resource == ingredient:
                        resources[resource] -= MENU[choice]["ingredients"][ingredient]
                        continue
            resources["Money"] += total
            if total > MENU[choice]["cost"]:
                change = total - MENU[choice]["cost"]
                resources["Money"] -= change
                print(f"Here is ${change} in change.")
            print(f"Here is your {choice}. Enjoy!")
        else:
            print("what a cheap-ass dude damn")

CoffeeMachine()