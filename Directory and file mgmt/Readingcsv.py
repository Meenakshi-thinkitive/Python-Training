import csv 
file_path = "Directory and file mgmt/program.csv"
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)