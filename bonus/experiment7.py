import json

csv_file = open('../file/csv_file.txt','r')

json_list=[]
with open('../file/csv_file.txt','r') as csv_file:
    for line in csv_file.readlines():
        club, city, country = line.strip().split(',')
        data = {
            'club': club,
            'city': city,
            'country': country
        }
        json_list.append(data)

with open('../file/json_file.txt','w') as json_file:
        json.dump(json_list, json_file)
