import os
import csv

electiondata_csv = os.path.join('.', 'Resources', 'election_data.csv')
print("Election Results")
print("-------------------------------")
votes = {}

with open(electiondata_csv) as f:
    f.readline()
    total_votes = 0
    for line in f:
        total_votes = total_votes + 1
        line = line.strip()
        line = line.split(",")
        candidates  = line[2]
        if candidates not in votes:
            votes [candidates] = 1
        else:
            votes [candidates] = votes [candidates] + 1
        
        
        
print("Total Votes: " , total_votes)
print("--------------------------------")
max_votes = 0
max_votes_candidate = ""
for candidate in votes:
    if votes [candidate] > max_votes:
        max_votes = votes [candidate]
        max_votes_candidate = candidate
    percent = votes[candidate]/total_votes*100
    print( f"{candidate}: {percent:.3f}% ({votes[candidate]})")
print("---------------------------------")
print("Winner: " + max_votes_candidate)
print("---------------------------------")
