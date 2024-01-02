curr_year = int(input("Year: "))

if curr_year % 4 == 0:
    if curr_year % 100 != 0:
        print(f"{curr_year} is a leap year.")
    elif curr_year % 400 == 0:
        print(f"{curr_year} is a leap year.")
    else:
        print(f"{curr_year} is not a leap year.")
else:
    print(f"{curr_year} is not a leap year.")