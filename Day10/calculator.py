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



def get_value(first_num, operator, second_num):
    if operator == '+':
        output = add(first_num, second_num)
    elif operator == '-':
        output = subtract(first_num, second_num)
    if operator == '*':
        output = multiply(first_num, second_num)
    if operator == "/":
        output = divide(first_num, second_num)
    print(f"{str(first_num)} {operator} {str(second_num)} = {str(output)}")
    return output


first_input = True
while True:
    first = int(input("Enter first number: "))
    operator = str(input("+\n-\n*\n/\nChoose an operator: "))
    second = int(input("Enter second number: "))
    if first_input:
        output = get_value(first, operator, second)
    else:
        
        output = get_value(first, operator, second)
    go_again = input(f"Type 'y to continue calculating with {output}, or type 'n' to start a new calc, or 'x' to quit: ").lower()
    if go_again == 'x':
        break
    if go_again == 'y':
        first_input = False
    else:
        first_input = True
# need to fix the continuing using number function flow
print("Thanks for using my calculator!")