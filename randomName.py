import random

name_list = []
count = 1

print("Please enter in names to this list. If you just type 'q' it will stop asking you for names and select a random name.")

while True:
    name = input(f"Name {count}:")
    count += 1
    if name == 'q':
        break
    name_list.append(name)

list_length = len(name_list)

rand_int = random.randint(0,list_length-1)
print(name_list[rand_int])