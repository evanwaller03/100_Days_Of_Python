line_one = ['-','-','-']
line_two = ['-','-','-']
line_three = ['-','-','-']
map = [line_one, line_two, line_three]

hiding_spot = input("Hide your treasure!\nSelection: ")

letter = hiding_spot[0].lower()
cols = ['a', 'b', 'c']

letter_index = cols.index(letter)
num_index = int(hiding_spot[1])-1

map[num_index][letter_index] = 'x'
print(f"{line_one}\n{line_two}\n{line_three}\n") 