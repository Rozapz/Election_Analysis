# The data we need to retrieve.
# The total number of votes cast
# A compelete list of candidates who recieved votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
#     print(election_data)


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

     # Write a header
#     txt_file.write("Counties in the election\n")

     # Write three counties to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson")

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#total vote
total_votes=0
# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
        # Read the file object with the reader function.

    # Print the header row.
    headers = next(file_reader)
    print(headers)


    for row in file_reader:
        #print(row)
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
             # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
#candidate_name=candidate_options(1)
#votes=candidate_votes[candidate_name]    
#vote_percentage = (votes / total_votes) * 100
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
vote_percentage_max=0
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    if vote_percentage > vote_percentage_max:
        Winner_name=candidate_name
        vote_percentage_max=vote_percentage

print(Winner_name)
# Print the candidate list.
print(candidate_options)
# Print the candidate vote dictionary.
print(candidate_votes)