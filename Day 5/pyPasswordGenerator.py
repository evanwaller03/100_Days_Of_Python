import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()'

l_count = int(input("How many letters would you like un your password?\n"))
n_count = int(input("How many numbers would you like?\n"))
s_count = int(input("How many symbols would you like?\n"))


letter_counter = 0 # SPOT 0
number_counter = 0 # SPOT 1
symbol_counter = 0 # SPOT 2

total = l_count+s_count+n_count

password = ""

while len(password) <= total:
    rand_int = random.randint(0,2)
    if rand_int == 0:
        if letter_counter < l_count:
            password = f"{password}{letters[random.randint(0,51)]}"
            letter_counter += 1
    
    elif rand_int == 1:
        if number_counter < n_count:
            password= f"{password}{(numbers[random.randint(0,9)])}"
            number_counter += 1
    
    elif rand_int == 2:
        if symbol_counter < s_count:
            password= f"{password}{symbols[random.randint(0,9)]}"
            symbol_counter += 1

print(f"Your New Password: {password}\nActual Length: {len(password)}\nRequested Total Length:{total}")