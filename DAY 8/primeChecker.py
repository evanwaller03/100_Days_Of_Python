user_input_satisfied = False

while not user_input_satisfied:
    user_num = int(input("Prime Number Checker: "))
    if type(user_num) == int and user_num <= 100 and user_num > 1:
        user_input_satisfied = True

prime_number = True
for n in range(2, int(user_num**0.5)+1):
    if user_num % n == 0:
        prime_number = False
        break

if prime_number:
    print(f"{user_num} is a prime number.")
else:
    print(f"{user_num} is not a prime number.")
