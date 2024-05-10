names = ["Evan", "Ian", "Meaghan", "Jerome", "Albert", "Karen", "Francesca", "David"]

long_names = [name.upper() for name in names if len(name) > 4]

print(long_names)