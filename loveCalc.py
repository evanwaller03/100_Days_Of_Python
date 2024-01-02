print("The Love Calc is calculating your score...")
name1 = str(input("Person 1: "))
name2 = str(input("Person 2: "))
combinedNames = name1+name2

digitOne = 0
digitTwo = 0
for letter in combinedNames:
    if letter.lower() in ('t', 'r', 'u', 'e'):
        digitOne += 1
    if letter.lower() in ('l', 'o', 'v', 'e'):
        digitTwo += 1

score = int(str(digitOne) + str(digitTwo))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")