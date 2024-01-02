print("The Love Calc is calculating your score...")
name1 = str(input("Person 1: "))
name2 = str(input("Person 2: "))
combinedNames = name1+name2
print(combinedNames)
print("---------------")

digitOne = 0
digitTwo = 0
for letter in combinedNames:
    if letter.lower() in ('t', 'r', 'u', 'e'):
        digitOne += 1
        print(letter)
    if letter.lower() in ('l', 'o', 'v', 'e'):
        digitTwo += 1

score = int(str(digitOne) + str(digitTwo))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")

elif score < 50 and score > 40:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")