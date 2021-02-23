#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#  * The total number of votes cast
#  * A complete list of candidates who received votes
#  * The percentage of votes each candidate won
#  * The total number of votes each candidate won
#  * The winner of the election based on popular vote.
#  * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#--------------------------------------------------------------------------------

# Import modules
import csv
import os

# store contents in variables, lists, and dictionaries
total_votes = 0
votes_candidate = {}
vote_percentage = {}
winner_votes = 0
# CSV file path
election_data_path = os.path.join("Resources", "election_data.csv")

# read and write in various formats
with open(election_data_path, newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')

# skips header row
    csvHeader = next(csvfile)
    for row in csvReader:

# total number of votes cast
        total_votes = total_votes + 1

# iterate through basic data structures
# list of each candidate, votes they received, and voting percentage for each
        candidate_name = row[2]
        if candidate_name in votes_candidate:
            votes_candidate[candidate_name] = votes_candidate[candidate_name] + 1
        else:
            votes_candidate[candidate_name] =1
# vote percentage per candidate, winner       )
    for candidate_name in votes_candidate:
        vote_percentage[candidate_name] = round((votes_candidate[candidate_name]/total_votes*100), 3)
# winning candidate
        if votes_candidate[candidate_name] > winner_votes:
            winner_votes = votes_candidate[candidate_name]
            winner = candidate_name
#print(total_votes)
#print(votes_candidate)
#print(vote_percentage)
#print(winner)
# Print to terminal
top_results = (f"Election Results\n----------------------------\nTotal Votes: {total_votes}\n----------------------------\n")
print(top_results)
for candidate_name in vote_percentage and votes_candidate:
    print(f"{candidate_name}: {vote_percentage[candidate_name]} % ({votes_candidate[candidate_name]})")
bottom_results = (f"----------------------------\nWinner: {winner}\n----------------------------")
print(bottom_results)
# export to txt file
election_results_path = os.path.join("Results", "pyPoll_Analysis.txt")
with open(election_results_path, "w") as text:
    text.write(top_results)
    for candidate_name in vote_percentage and votes_candidate:
        text.write(f"{candidate_name}: {vote_percentage[candidate_name]} % ({votes_candidate[candidate_name]})\n")
    text.write(bottom_results)
# debug along the way