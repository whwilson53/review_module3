#The data we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path.
path_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a pth.
path_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(path_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)



#1. the total number of votes cast
#2. A complete list of canddidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote