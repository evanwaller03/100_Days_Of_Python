# Rules
# Add up cards tp the largest number
# Numbers are face value
# Face cards are all 10
# Ace can either be 1 or 11
# If the dealer is less than 17 they must hit
# If you go over 21 you lose

# When your score equals the dealers score then there is a draw


# 52 Cards, 13 Aces, 13 Clubs, 13 Diamonds, 13 Hearts
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
import random 

individual_13 = {
    "2" : 2, # Card and then order for comparing their values later, 2 is the lowest, ace is the highest
    "3" : 3, 
    "4" : 4, 
    "5" : 5,
    "6" : 6,
    "7" : 7, 
    "8" : 8, 
    "9" : 9, 
    "10" : 10, 
    "J" : 10, 
    "Q" : 10, 
    "K" : 10, 
    "A" : 10,
}

suits = [ "C", "D", "H", "S" ]

deck = []

for suit in suits:
    for num in individual_13:
        card_to_add = num + suit
        deck.append(card_to_add)

win_flag = True
randomized_deck = deck
random.shuffle(randomized_deck)

player_hand = []
dealer_hand = []

def deal_hand(player_hand, dealer_hand, deck):
    i = 0
    while i < 4:
        random_card = deck[random.randint(0,len(deck)-1)]
        if i % 2 == 0:
            player_hand.append(random_card)

        if i % 2 == 1:
            dealer_hand.append(random_card)

        deck.remove(random_card)
        i += 1
    print(f"Your Cards: {player_hand[0]}, {player_hand[1]}")
    print(f"Dealer's Hand: {dealer_hand[1]}, ??\n")

def draw_card(deck, user):
    random_card = deck[random.randint(0,len(deck)-1)]
    if user == 'p':  #player hits
        player_hand.append(random_card)

    else:  #dealer hits
        dealer_hand.append(random_card)
    deck.remove(random_card)

def calc_value(hand):
    hand_val = 0
    for card in hand:
        hand_val += individual_13[card[:-1]]

    return hand_val

# Player and Dealer now get their initial hand
deal_hand(player_hand, dealer_hand, randomized_deck)
while True: 
    if input("Do you want to draw another card? (Y) or (N): ").lower() == 'y':
        draw_card(randomized_deck, 'p')
        hand_value = calc_value(player_hand)
        string_players_hand = ", ".join(player_hand)
        print(f"Your Cards: {string_players_hand}  (Value: {hand_value})")
        if hand_value > 21:
            win_flag = False
            break

    else:
        break
if win_flag:
    string_players_hand = ", ".join(player_hand)
    print(f"Your Cards: {string_players_hand}")

    dealer_hand_value = calc_value(dealer_hand)

    while dealer_hand_value < 17:
        draw_card(dealer_hand, 'd')
        dealer_hand_value = calc_value(dealer_hand)

    if dealer_hand_value > 21:
        print("You win")
    elif hand_value > dealer_hand_value:
        print("You win!")
    elif hand_value < dealer_hand_value:
        print("You lose.")
    else:
        print("Draw.")
else:
    print("You lose.")
        


