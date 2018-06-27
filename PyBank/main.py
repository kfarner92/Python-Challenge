import os 
import csv
#Source filepath
csvpath = os.path.join('..','PyBank','budget_data.csv')
# Storage Lists and variables
netProfitLoss = 0
row_count = 0
months = []
revenue = []
#open and read csv
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    for row in csvreader:
        netProfitLoss = netProfitLoss + int(row[1])
        row_count = row_count + 1
        months.append(row[0])
        revenue.append(int(row[1]))
#storing greatest increase and decrease values
moneyWaterfall = revenue[0]
burningBenjamins = revenue[0]
for row in range(len(revenue)):
    if revenue[row] >= moneyWaterfall:
        moneyWaterfall = revenue[row]
        bestMonth = months[row]
    elif revenue[row] <= burningBenjamins:
        burningBenjamins = revenue[row]
        worstMonth = months[row]
#getting the average revenue amount
averageRevenue = round(netProfitLoss/row_count)

outputLocation = os.path.join('../Pybank/Pybank_Final.txt')
with open(outputLocation,'w') as writeFile:
    writeFile.writelines('Financial Analysis\n')
    writeFile.writelines('------------------------------'+ '\n')
    writeFile.writelines('Total Months: '+str(row_count) + '\n')
    writeFile.writelines('Total Profit/Loss: $' +str(netProfitLoss) + '\n')
    writeFile.writelines('Average Change: $' + str(averageRevenue) + '\n')
    writeFile.writelines('Greatest Increase in Profits: '+str(bestMonth) +' ($'+str(moneyWaterfall)+')' + '\n')
    writeFile.writelines('Greatest Decrease in Profits: '+str(worstMonth) +' ($'+str(burningBenjamins)+')' + '\n')

with open(outputLocation, 'r') as readFile:
    print (readFile.read())
#testing
#print(averageRevenue)
#print(netProfitLoss)
#print(row_count)
#print(burningBenjamins)
#print(worstMonth)
#print(moneyWaterfall)
#print(bestMonth)
# row_count = sum(1 for row in csvreader)