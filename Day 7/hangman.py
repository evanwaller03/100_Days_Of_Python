import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

random_words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "indigo", "jackfruit",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine",
    "umbrella", "vanilla", "walnut", "xenia", "yellow", "zucchini", "amber", "bronze", "copper", "diamond",
    "emerald", "fuchsia", "gold", "heliotrope", "ivory", "jade", "krypton", "lapis", "malachite", "nickel",
    "onyx", "pearl", "quartz", "ruby", "sapphire", "topaz", "uranium", "violet", "wax", "xenon", "yellowish", "zircon",
    "artist", "baker", "carpenter", "driver", "engineer", "farmer", "gardener", "hunter", "illustrator", "jeweler",
    "knight", "librarian", "musician", "nurse", "officer", "painter", "queen", "ranger", "scientist", "teacher",
    "umpire", "veteran", "waiter", "xenophile", "yogini", "zoologist", "almond", "biscuit", "cookie", "donut",
    "eclair", "flan", "gelato", "hazelnut", "icing", "jelly", "kale", "lettuce", "mustard", "nougat",
    "olive", "pistachio", "quinoa", "raisin", "spinach", "tomato", "utopia", "vanish", "walrus", "xylem",
    "yacht", "zebra"
]
play_again = True

while play_again:

    selected_word = random_words[random.randint(0,100)].lower()
    blanks = ""
    for n in range(0, len(selected_word)):
        blanks = blanks + "_"

    lives_left = 6
    letter_bank = []

    print(blanks)

    correct_word = False
    user_win = True

    while correct_word == False:
        print(HANGMANPICS[6-lives_left])
        print(blanks)
        if len(letter_bank) > 0:
            print(f"Letters used: {str(", ".join(letter_bank))}")
        print(f"Lives left: {lives_left}")

        guess = input("Guess a letter: ").lower()
        if guess not in letter_bank:
            letter_bank.append(guess)
            if str(guess) in selected_word:
                for n in range(0, len(selected_word)):
                    if selected_word[n] == guess:
                        blanks = blanks[:n] + guess + blanks[n + 1:]
                if "_" not in blanks:
                    break
                
            else: 
                print(f"\"{guess.lower()}\" is not in the word.")
                if lives_left > 0:
                    lives_left -= 1
                    if lives_left == 0:
                        user_win = False
                        break
                
        else:
            print("That letter has already been used.")

    if user_win:
        print(selected_word)
        print("You Win!")
    else:
        print(blanks)
        print(f"The correct word was: {selected_word}")
        print("You lost. :(")

    play_again_input = str(input("You Lost. Play again? Yes(Y) or No(N)?")).lower()
    if play_again_input == "y":
        play_again = True
    elif play_again_input == "n":
        play_again = False

print("Thanks for playing!")
    