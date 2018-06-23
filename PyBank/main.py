import os 
import csv
#Source filepath
csvpath = os.path.join('..','PyBank','budget_data.csv')
# Storage Lists
date = []
revenue = []

with open(csvpath,newline='')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
cleaned_csv = zip(date,revenue)
output_file = os.path.join('..','PyBank','PyBank_Final.csv')
with open(output_file, 'W', newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["date","revenue"])
    csvwriter.writerows(cleaned_csv)

#    print(csvreader)

#   csv_header = next(csvreader)ß
#   print(f"CSV Header: {csv_header}")
#   for row in csvreader:
#       print (row)