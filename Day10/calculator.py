import os
print("Welcome to the calculator app.")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_value(first_num, operator, second_num):
    output = operations[operator](first_num, second_num)
    print(f"{str(first_num)} {operator} {str(second_num)} = {str(output)}")
    return output

def calculator():
    first = int(input("Enter first number: "))
    for symbol in operations:
        print(symbol)

    continue_operation = True

    while continue_operation:
        operator = str(input("Choose an operator: "))
        second = int(input("Enter second number: "))
        output = get_value(first, operator, second)

        go_again = input(f"Type 'y to continue calculating with {output}, or type 'n' to start a new calc, or 'x' to quit: ").lower()
        if go_again == 'x':
            print("Thanks for using my calculator!")
            break
        if go_again == 'y':
            first = output

        else:
            continue_operation = False
            calculator()

calculator()
