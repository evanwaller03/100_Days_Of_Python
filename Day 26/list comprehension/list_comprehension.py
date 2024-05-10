names = ["Evan", "Ian", "Meaghan", "Jerome", "Albert", "Karen", "Francesca", "David"]

long_names = [name.upper() for name in names if len(name) > 4]

print(long_names)

nums = [1,1,2,3,4,5,6,7,8,9]

squared_nums = [n*n for n in nums]

print(squared_nums)

list_of_strings = input().split(',')

convert = [int(n) for n in list_of_strings if (int(n) % 2) == 0]

print(convert)