import pandas

user_input = input("Enter a word: ").upper()

data = pandas.read_csv("Day 26/nato alphabet project/nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

conversion = [phonetic_dictionary[letter] for letter in user_input]

print(conversion)