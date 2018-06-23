import os 

import csv

cvspath = os.path.join('Users','KFarner','BootCamp','Python-Challenge','PyBank','budget_data.csv')

with open(cvspath,newline='')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print (row)