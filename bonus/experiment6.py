import csv
movies = [
    {"name": "The Matrix","director":"Wachowski"},
    {"name": "Green Book","director": "Farrelly"},
    {"name":"Amadeus","director":"Forman"}
]
# def write_to_file(output):
#         with open("../file/file.csv","w") as f:
#             f.write("name,director\n")
#             for line in output:
#                 f.write(f"{line['name']},{line['director']}\n")
def write_to_file(output):
        with open("../file/file.csv","w") as f:
            writer = csv.DictWriter(f, fieldnames=["name","director"])
            writer.writeheader()
            writer.writerows(output)

def read_from_file():
    with open("../file/file.csv", "w") as f:
        reader = csv.DictReader(f)
        for line in reader:
            columns = line.strip().split(",")
            print(f"Name: {columns[0]}\tDirector: {columns[1]}")

write_to_file(movies)