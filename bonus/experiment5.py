with open('../file/csv_data.csv','r') as file:
    content = file.readlines()

lines = [line.strip().split(",") for line in content]

for line in lines:
    name = line[0]
    age = line[1]
    university = line[2]
    degree = line[3]

    print(f'{name} is {age}, studying {degree} at {university}')


