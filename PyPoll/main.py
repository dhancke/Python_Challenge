# File path associated with the file across OS
import os

# Module for reading CSV files:
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
# Read header row first:
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

# Parameters forthe variables below:
    total_votes = 0
    candidates = {}
    row_count = 0
    win_count = 0
    winner = ""

# The total number of votes cast and dictionary of candidates:
    for row in csvreader:
        row_count += 1
        candidate = row[2]
        if candidate not in candidates:
    #If it is a new candidate, then add the candidate name and vote count of 1
            candidates[candidate] = {"name": candidate, "vote_count": 1}
            total_votes += 1
        else: 
    #If it is an existing candidate, then increment the vote count
            candidates[candidate]["vote_count"] += 1
            total_votes += 1

 #Calculate vote % for each candidate:
    print("Election Results")
    print("-----------------")
    print(f"total votes: {total_votes}") 
    print("-----------------")

    for candidate, vote_count in candidates.items(): 
        candidate_name = candidates[candidate]["name"] 
        candidate_vote_count = candidates[candidate]["vote_count"]    
        candidate_vote_percentage = (candidate_vote_count / total_votes) * 100
        print(f"{candidate_name}: {candidate_vote_percentage:.3f}% ({candidate_vote_count})")

# Calculate the winner
        if candidate_vote_count >= win_count:
            winner = candidate_name
            win_count = candidate_vote_count
    print("-----------------")
    print(f"Winner: {winner}") 
    print("-----------------")      

# Module for writing output files:
outputpath = os.path.join('Analysis', 'output.txt')
with open(outputpath, 'w') as file:
    file.writelines("Election Results \n")
    file.writelines("----------------\n")
    file.writelines("Total Votes: " + str(total_votes) + "\n")
    file.writelines("----------------\n")
    
    for candidate, vote_count in candidates.items(): 
        candidate_name = candidates[candidate]["name"] 
        candidate_vote_count = candidates[candidate]["vote_count"]    
        candidate_vote_percentage = (candidate_vote_count / total_votes) * 100
        file.writelines(candidate_name + ": ")
        file.writelines(str(candidate_vote_percentage) + "% (")
        file.writelines(str(candidate_vote_count) + ") \n")

# Calculate the winner
        if candidate_vote_count >= win_count:
            winner = candidate_name
            win_count = candidate_vote_count
    file.writelines("----------------\n")
    file.writelines("Winner: " + winner + "\n")
    file.writelines("----------------\n")