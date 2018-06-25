import os 
import csv
#Source filepath
csvpath = os.path.join('..','PyBank','budget_data.csv')
# Storage Lists

totalMonths = 0
netProfitLoss = 0
largestAvgChange = 0.00
largestProfit = 0
largestLoss = 0

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    for row in csvreader:
 #       totalMonths = totalMonths + int(count(row[0]))
        netProfitLoss = netProfitLoss + int(row[1])
#print(netProfitLoss)
