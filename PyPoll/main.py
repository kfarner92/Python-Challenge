import os
import csv
import numpy
#Source filepath
csvpath = os.path.join('..','PyPoll','election_data.csv')

#empty lists and var
candidates = []
num_votes = 0
vote_counts = []

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    for row in csvreader:
        
        num_votes = num_votes + 1

        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#make csv
outputLocation = os.path.join('../PyPoll/PyPoll_Final.txt')
with open(outputLocation,'w') as writeFile:
    writeFile.writelines("Election Results\n")
    writeFile.writelines("--------------------------\n")
    writeFile.writelines(f"Total Votes: {num_votes}\n")
    for count in range(len(candidates)):
        writeFile.writelines(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    writeFile.writelines("---------------------------\n")
    writeFile.writelines(f"Winner: {winner}\n")
    writeFile.writelines("---------------------------\n")