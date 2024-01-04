rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

random_integer = random.randint(0,2)

while True:

    your_input = int(input("Welcome to rock paper scissors. Type 0 for Rock, 1 for Paper, 2 for Scissors. Go!\nYour Choice:\n"))

    if your_input == 0:
        your_choice = rock
    if your_input == 1:
        your_choice = paper
    if your_input == 2:
        your_choice = scissors

    if random_integer == 0:
        opponents_choice = rock
    if random_integer == 1:
        opponents_choice = paper
    if random_integer == 2:
        opponents_choice = scissors

    print(your_choice)
    print("Your Opponent's Choice:\n" + opponents_choice)

    if your_input == random_integer:
        print("Tie game.")
    elif your_input == 0 and opponents_choice == 1:
        print("You lose.")
    elif your_input == 1 and opponents_choice == 2:
        print("You lose.")
    elif your_input == 2 and opponents_choice == 0:
        print("You lose.")
    elif your_input == 1 and opponents_choice == 0:
        print("You win.")
    elif your_input == 2 and opponents_choice == 1:
        print("You win.")
    else:
        print("You win.")
    
    play_again = input("Play again? (Y or N)")
    if play_again.lower() == 'n':
        break