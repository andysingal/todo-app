""""
https://teclado.com/30-days-of-python/python-30-day-14-files/
"""

with open('../file/iris.csv',"r") as file:
    iris_data = file.readlines()
print(iris_data)
headers = iris_data[0].strip().split(",")
irises = []

for row in iris_data[1:]:
     iris = row.strip().split(",")
     iris_dict = dict(zip(headers,iris))
     irises.append(iris_dict)

print(irises)

