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

is_on = True

while is_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == 'report':
        print_report()
    elif user_order == 'off':
        is_on = False
    else:
        print(WATER)
        drink = MENU[user_order]
        WATER = check_resources_available(drink, WATER, MILK, COFFEE)
        print(WATER)