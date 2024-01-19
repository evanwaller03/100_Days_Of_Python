# Recreate the coffe machine but with Object Oriented Programming

# Attributes: variables associated with the object
# Methods: functions that the object can call to execute
# Class: Blue print for objects that you use in your code
# Classes are named with PascalCasing
# car == CarBluePrint()
# object == Class()

from COFFEEMACHINE.menu import Menu, MenuItem
from COFFEEMACHINE.coffee_maker import CoffeeMaker
from COFFEEMACHINE.money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

def start_machine():
    is_on = True
    while is_on:
        user_order = str(input(f"What would you like? {menu.get_items()}: "))
        if user_order == 'report':
            coffee_machine.report()
        elif user_order == 'off':
            is_on = False
        else:
            drink = menu.find_drink(user_order)
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

start_machine()