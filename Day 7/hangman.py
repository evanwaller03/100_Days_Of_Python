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

lives_left = 6

selected_word = random_words[random.randint(0,100)]
blanks = ""
for n in range(0, len(selected_word)):
    blanks = blanks + "_ "

print(selected_word)
print(blanks)
