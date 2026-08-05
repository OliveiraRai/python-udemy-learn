from menu import resources

class MoneyMachine:
    def report():
        print(f"Money: ${resources['Money']}")

    def make_payment(cost: float):
        penny = float(input("How many pennies? "))
        nickel = float(input("How many nickels? "))
        dime = float(input("How many dimes? "))
        quarter = float(input("How many quarters? "))
        payment = (penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25)
        if payment >= cost:
            return True
        else:
            return False