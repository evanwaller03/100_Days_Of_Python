from data import MENU, resources

WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
MONEY = 0

def print_report():
    print(f"Water: {WATER}\nMilk: {MILK}\nCoffee: {COFFEE}\nMoney: ${MONEY}")

def check_resources_available(drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("Number of Quarters: ")) * .25
    total += int(input("Number of Dimes: ")) * .1
    total += int(input("Number of Nickels: ")) * .05
    total += int(input("Number of Pennies: ")) * .01
    return total    

is_on = True

while is_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == 'report':
        print_report()
    elif user_order == 'off':
        is_on = False
    else:
        drink = MENU[user_order]
        print(drink)
        if check_resources_available(drink['ingredients']):
            payment = process_coins()
            if payment < drink['cost']:
                print(f"Sorry, please enter more change to buy {drink}")
            else:
                MONEY += payment
                for ingredient in drink['ingredients']:
                    resources[ingredient] -= drink['ingredients'][ingredient]
                        