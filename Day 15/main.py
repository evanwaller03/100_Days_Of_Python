from data import MENU, resources

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0

def print_report():
    print(f"Water: {WATER}\nMilk: {MILK}\nCoffee: {COFFEE}\nMoney: {MONEY}")

def check_resources_available(drink, WATER, MILK, COFFEE):
    WATER -= drink['ingredients']['water']
    return WATER

def get_order ():
    global WATER
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == 'report':
        print_report()
    print(WATER)
    drink = MENU[user_order]
    WATER = check_resources_available(drink, WATER, MILK, COFFEE)
    print(WATER)

get_order()