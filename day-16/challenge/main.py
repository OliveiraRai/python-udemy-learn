import menu, money_machine, coffee_maker, utils

handleMenu = menu.Menu
handleCoffee = coffee_maker.CoffeeMaker
handleMoney = money_machine.MoneyMachine

def coffeeMachine():
    while True:
        print("Choose your order by typing the number:")
        handleMenu.get_items()
        choice = input("Choice: ")
        match choice:
            case "":
                utils.message()
                continue
            case "report":
                utils.clear()
                handleCoffee.report()
                utils.wait()
                continue
            case "profit":
                utils.clear()
                handleMoney.report()
                utils.wait()
                continue
            case str() if choice.isdigit():
                utils.message()
                continue
            case "espresso" | "latte" | "cappuccino":
                utils.clear()
                order = handleMenu.find_drink(choice)
                if not handleCoffee.is_resource_sufficient(order):
                    utils.customMessage("Insufficient resources.")
                    continue
                is_money_accepted, change = handleMoney.make_payment(order.cost)
                if not is_money_accepted:
                    utils.customMessage("Insufficient money.")
                    continue
                handleCoffee.make_coffee(order)
                utils.customMessage(f"Here is your {choice} and you ${change} change. Enjoy!")
            case _:
                utils.message()
        

coffeeMachine()