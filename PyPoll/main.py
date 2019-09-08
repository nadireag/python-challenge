# Import modules
import os
import csv

# Specify the path for csv file
csvpath = os.path.join("election_data.csv")

# Create lists to hold info
voter_id = []
county = []
candidate = []

# print the text
print("Election Results")
print("-------------------------")

# Open the file to read csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # read header first
    csv_header = next(csvreader)

    # loop through the rows to add items to the lists
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    # Find total votes
    total_votes = len(voter_id)
    print(f"Total Votes:  {total_votes}")
    print("-------------------------")

    # Find candidate names
    candidate_names = []
    for row in candidate:
        if row not in candidate_names:
            candidate_names.append(row)
    #print(candidate_names)

    # Find each candidate's total votes
    #candidate_votes = 0
    #for name in candidate_names:
        #for row in candidate:
            #if name == row:
                #candidate_votes +=1
    #print(f"{name} {candidate_votes}")
           

    #print(candidate_votes)
    
    #percentage = round(candidate_votes / total_votes * 100 , 2)

    #print(f"{name}: {percentage}% ({candidate_votes})")

    

print(f'-------------------------')

# Write the results to the output file
# create a path for the output file
output_file = os.path.join("vote_counting.txt")

# open the file to write text
with open(output_file, "w") as text:
    
    text.write("Election Results\n")
    text.write(f"------------------------\n")
    text.write(f"Total Votes:  {total_votes}\n")
    text.write(f"------------------------\n")
    