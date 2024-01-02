party_names = []
print("Welcome to Evan's tip calculator.")
total_bill = float(input("Total bill amount: $"))
party_size = int(input("How many people will split the bill: "))
#total_tax = float(input("Total tax amount: $"))
i = 0
print("Please enter the name of each party member:")
while i < party_size:
    party_names.append(input("Person " + str(i+1) + ": "))
    i += 1
tip_percent = float(input("What percetnage tip would you like to give: "))
per_person = (total_bill+(total_bill*tip_percent))/party_size

# How to round a float
final_amount = "{:.2f}".format(per_person)
#print(type(tip_percent)) //learn more about types
print(f"Each person must pay: ${final_amount}")
for person in party_names:
    print(f"{person} must pay: {final_amount}")

