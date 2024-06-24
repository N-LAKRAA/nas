import csv 

with open("valeurs_annuelles.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    data = list(reader)
    
    for row in data:
        row.pop()
        print(row)
    csv_file.close()