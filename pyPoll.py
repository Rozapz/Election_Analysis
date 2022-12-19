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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
        # Read the file object with the reader function.

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    
#    for row in file_reader:
#        print(row)