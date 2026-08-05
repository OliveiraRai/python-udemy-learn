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

class MenuItem:
    def __init__(self, name: str, cost: float, ingredients: dict[str]):
        self.name = name
        self.cost = cost
        self.ingredients = dict(ingredients)
        
class Menu:
    def get_items():
        i = 0
        for item in MENU:
            i += 1
            print(f"{i}. {item}")

    def find_drink(order_name: str):
        if order_name in MENU:
            return MenuItem(order_name, MENU[order_name]["cost"], MENU[order_name]["ingredients"])
        else:
            return None
            
