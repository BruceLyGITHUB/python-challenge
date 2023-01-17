import os
import csv

#collect data from directory
polling = os.path.join(".","Resources","election_data.csv")

#read csv
with open(polling, newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #total votes
    next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)

    #candidates who received votes
    candidatelist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidatelist: 
            candidatelist.append(candidate)
    candidatecount = len(candidatelist)

    #percentage of votes for each candidate
    votes = list()
    percentage = list()
    for j in range (0,candidatecount):
        name = candidatelist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

    #total number of votes each candidate won
    

    #winner of election
    winner = votes.index(max(votes))    

    #terminal print
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candidatecount): 
        print(f"{candidatelist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidatelist[winner]}")
    print("----------------------------")

    #txt print
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,candidatecount): 
        print(f"{candidatelist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candidatelist[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))