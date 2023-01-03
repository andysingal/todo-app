# import glob
#
# myfiles = glob.glob("file/*.txt")
#
# for filepath in myfiles:
#     with open(filepath,'r') as file:
#         print(file.read())

import csv

with open("file/weather.csv", 'r') as files:
    data = list(csv.reader(files))

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
         print(row[1])
