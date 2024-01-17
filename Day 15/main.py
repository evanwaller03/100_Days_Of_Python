from data import MENU, resources

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0

def print_report():
    print(f"Water: {WATER}\nMilk: {MILK}\nCoffee: {COFFEE}\nMoney: ${MONEY}")

def check_resources_available(drink):
    for ingredient in drink:
        if drink[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coint():
    print("Please insert coins.")
    total = int(input("Number of Quarters: ")) * .25
    total += int(input("Number of Dimes: ")) * .1
    total += int(input("Number of Nickels: ")) * .05
    total += int(input("Number of Pennies: ")) * .01
    

is_on = True

while is_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == 'report':
        print_report()
    elif user_order == 'off':
        is_on = False
    else:
        drink = MENU[user_order]
        if check_resources_available(drink):
