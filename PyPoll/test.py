import os
import csv

filename = open('election_data.csv', 'r')
file = csv.DictReader(election_data.csv)

candidate = []

for col in file:
    candidate.append(col['candidate'])

print(candidate)