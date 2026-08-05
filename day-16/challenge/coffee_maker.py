import menu

class CoffeeMaker:
    def report():
        for resource in menu.resources:
            match resource:
                case "Water":
                    print(f"{resource}: {menu.resources[resource]}ml")
                case "Milk":
                    print(f"{resource}: {menu.resources[resource]}ml")
                case "Coffee":
                    print(f"{resource}: {menu.resources[resource]}g")    

    def is_resource_sufficient(drink: menu.MenuItem):
        for ingredient in drink.ingredients:
            if menu.resources[ingredient] < drink.ingredients[ingredient]:
                return False
        return True

    def make_coffee(order: menu.MenuItem):
        for ingredient in order.ingredients:
            menu.resources[ingredient] -= order.ingredients[ingredient]


