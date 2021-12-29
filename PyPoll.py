#The data we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path.
path_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a pth.
path_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize accumulator for total votes
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(path_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
    
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_percentage = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
        
        
    

        
        print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n of the vote.")
        


#1. the total number of votes cast
#2. A complete list of canddidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote