from menu import resources, MenuItem

class CoffeeMaker:
    def report():
        for resource in resources:
            match resource:
                case "Water":
                    print(f"{resource}: {resources[resource]}ml")
                case "Milk":
                    print(f"{resource}: {resources[resource]}ml")
                case "Coffee":
                    print(f"{resource}: {resources[resource]}g")    

    def is_resource_sufficient(drink: MenuItem):
        pass # TODO

    def make_coffee(order: MenuItem):
        pass # TODO