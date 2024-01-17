from data import MENU, resources

MONEY = 0

def print_report():
    print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${MONEY}")

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

def transaction_complete(money_received, drink_cost):
    if money_received >= drink_cost:
        global MONEY
        MONEY += payment
        change = round(money_received - drink_cost,2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry, that is not enough money.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= drink['ingredients'][ingredient]
    print(f'Here is your {drink_name}.')

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
            if transaction_complete(payment, drink['cost']):
                make_coffee(user_order, drink['ingredients'])
                        