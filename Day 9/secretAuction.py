print("Welcome to the secret Auction!")

bidders = {}

while True:
    bidder_to_add = input("Please enter the name of the bidder: ")
    price_to_add = int(input("Please enter their bid amount: "))
    bidders[bidder_to_add] = price_to_add
    go_again = input("Enter another bidder? (Y) or (N)").lower()
    if go_again == 'n':
        break

max_bid = 0
max_bidder = ''

for person in bidders:
    if max_bid < bidders[person]:
        max_bid = bidders[person]
        max_bidder = person

print(f"The max bidder, {max_bidder.capitalize()}, paid ${max_bid}.")