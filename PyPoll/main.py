import os
import csv
import numpy

csvpath = os.path.join('..', 'PyPoll','election_data.csv')

correy_count = []
khan_count = []
li_count = []
oTooley_count = []

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    for row in csvreader:
        if row[2] == "Correy":
            correy_count.append(str(row[2]))
        if row[2] == "Khan":
            khan_count.append(str(row[2]))
        if row[2] == "Li":
            li_count.append(str(row[2]))   
        if row[2] == "O'Tooley":
            oTooley_count.append(str(row[2]))      
