print("Welcome to Python Pizza. How can Evan help you today?")
size = str(input("Do you want a S, M, or L pizza: ")) # 15, 20, 25
add_pep = str(input("Do you want to add pepperoni (Y or N): ")) # S: $2 M&L: $3
add_cheese = str(input("Do you want to add cheese (Y or N): ")) # 1

# Handle Size
if size == "S":
    price = 15
if size == "M":
    price = 20
if size == "L":
    price = 25

# Handle Pepperoni
if add_pep == "Y":
    if size == "S":
        price += 2
    else:
        price += 3


# Handle Cheese
if add_cheese == "Y":
    price += 1


print(f"Pizza Price: {price}")