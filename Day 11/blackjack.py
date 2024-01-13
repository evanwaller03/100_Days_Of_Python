# 52 Cards, 13 Aces, 13 Clubs, 13 Diamonds, 13 Hearts
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
import random 

individual_13 = {
    "2" : 1, # Card and then order for comparing their values later, 2 is the lowest, ace is the highest
    "3" : 2, 
    "4" : 3, 
    "5" : 4,
    "6" : 5,
    "7" : 6, 
    "8" : 7, 
    "9" : 8, 
    "10" : 9, 
    "J" : 10, 
    "Q" : 11, 
    "K" : 12, 
    "A" : 13,
}

suits = [ "C", "D", "H", "S" ]

deck = []

for suit in suits:
    for num in individual_13:
        card_to_add = num + suit
        deck.append(card_to_add)

print(deck)
random.shuffle(deck)
print(deck)

