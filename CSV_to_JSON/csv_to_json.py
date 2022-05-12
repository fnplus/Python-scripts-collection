import csv
import json

file_name = input("Provide the CSV filename : ")
if not file_name.strip().endswith(".csv"):
    file_name += ".csv"

with open(file_name) as f:
    reader = csv.reader(f, delimiter=",")

    titles = next(reader)
    temp_data = []
    
    for row in reader:
        temp_data.append({col: val for col, val in zip(titles, row)})

with open(file_name.strip()[:-4] + ".json", "w") as f_j:
    json.dump(temp_data, f_j, indent=4)

print("File converted successfully :)\n")