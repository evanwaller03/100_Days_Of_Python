from data import MENU, resources

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]

def print_report():
    return 0

def get_order ():
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == 'report':
        print_report()
