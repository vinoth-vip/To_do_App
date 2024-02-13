import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

Climate = input("Enter the value:")

for row in data[1:]:
    if row[0] == Climate:
        print(row[1])
