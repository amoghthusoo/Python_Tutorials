import csv

data = []

with open("AIML_Lab\Linear_Regression (From Scratch)\Salary Data.csv", "r") as f:
    reader = csv.reader(f)
    
    for row in reader:
        data.append(row)

for i in range(10):
    print(data[i])