#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as example:
    starting_letter = example.read()

for name in names:
    new_letter = starting_letter.replace(PLACEHOLDER,name.strip())
    file_name = f"Day 24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt"
    new_file = open(file_name, "w")
    new_file.write(new_letter)
    