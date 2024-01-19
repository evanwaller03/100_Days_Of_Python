from prettytable import PrettyTable

table = PrettyTable()
 
table.add_column("Pokemon Name", ["Pikachu", "Deez Nuts", "Hello"])
table.add_column("Type", ["Electric", "Funny", "Welcome"])
table.align = 'l'
print(table)