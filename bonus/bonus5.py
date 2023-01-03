def read_file():
    with open('../bonus/file/data.txt','r') as f:
        lines = [line.strip() for line in f.readlines()]

    values = lines[1:]
    values = [float(i) for i in values]

    average = sum(values)/len(values)
    return average

average = read_file()
print(read_file())