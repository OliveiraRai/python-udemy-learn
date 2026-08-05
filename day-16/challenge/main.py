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
            case str() if not choice.isdigit():
                utils.message()
                continue
            case "1" | "2" | "3":
                pass # TODO
            case _:
                utils.message()
        

coffeeMachine()