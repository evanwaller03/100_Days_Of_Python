import random

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

selected_word = random_words[random.randint(0,100)].lower()
blanks = ""
for n in range(0, len(selected_word)):
    blanks = blanks + "_"

lives_left = 6
letter_bank = []

print(selected_word)
print(blanks)

correct_word = False
user_win = True

while correct_word == False:
    print(f"Lives left: {lives_left}")
    guess = input("Guess a letter: ").lower()
    if guess not in letter_bank:
        letter_bank.append(guess)
        if str(guess) in selected_word:
            print("Correct!")
            #replace a blank
            for n in range(0, len(selected_word)):
                if selected_word[n] == guess:
                    blanks = blanks[:n] + guess + blanks[n + 1:]
            if "_" not in blanks:
                break
            
            print(blanks)
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
    print("You Win!")
    # while True:
    #     play_again = str(input("You Lost. Play again? Yes(Y) or No(N)?")).lower()
    #     if play_again == "y":
            
    #     elif play_again == "n":
else:
    print("You lost. :(")

            
    