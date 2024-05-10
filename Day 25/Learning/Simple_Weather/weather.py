import csv

with open("Day 25/Weather_Data/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temps = []
    for row in data:
        if row[1] != "temp":
            temps.append(row[1])

for temp in temps:
    print(temp)

