# Import modules
import os
import csv

# Specify the path for csv file
csvpath = os.path.join("election_data.csv")

# Create lists to hold info
voter_id = []
county = []
candidate = []
winner = 0
winner_candidate = ""

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

    # Find each candidate's total vote, and percentage
    for i in range(0,len(candidate_names)):
        vote_count = 0
        for row in candidate:    
            if row == candidate_names[i]:
                vote_count +=1
                percentage = round(vote_count / total_votes * 100, 2)
                if percentage > winner:
                    winner = percentage
                    winner_candidate = candidate_names[i]
    
            
        print(f"{candidate_names[i]}: {percentage}% ({vote_count})") 
    print(f'-------------------------')
    print(f"Winner: {winner_candidate}")        
print(f'-------------------------')
        
# Write the results to the output file
# create a path for the output file
output_file = ("vote_counting.txt")

# open the file to write text
with open(output_file, "w") as text:
    
    text.write("Election Results\n")
    text.write(f"------------------------\n")
    text.write(f"Total Votes:  {total_votes}\n")
    text.write(f"------------------------\n")
    for i in range(0,len(candidate_names)):
        text.write(f"{candidate_names[i]}: {percentage}% ({vote_count})\n")
    text.write(f"------------------------\n")
    text.write(f"Winner: {winner_candidate}\n")
    text.write(f'------------------------\n')




    