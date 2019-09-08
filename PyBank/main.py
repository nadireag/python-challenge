# Import modules 
import os
import csv

# Specify the path for the csv file
csvpath = os.path.join("budget_data.csv")

# create lists to hold monts and profit/losses and change info
months = []
profit_loss = []
change = []
date = []

# Open the file to read
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # read the header
    csv_header = next(csvreader)

    # append months and profit loss info to the lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # print information to the terminal
    print("Financial Analysis")
    print("--------------------------")

    # Calculate the total number of months 
    total_months = len(months)
    print(f"Total Months: {total_months}")

    # loop through the list to calculate  the net total profit/losses
    total = 0
    for row in profit_loss:
        total += (row)

    # print total_profit_loss
    print(f"Total: ${total}")

    #  Create change list to hold info
    for i in range(0,(len(profit_loss)-1)):
        change.append(int(profit_loss[i+1]) - int(profit_loss[i]))

    # Find average change
    total_change = 0
    for row in change:
        total_change +=row
    average_change = round(total_change / len(change),2)

    print(f"Average Change: ${average_change}")

    # Find greatest increase and decrease
    greatest_increase = max(change)
    greatest_decrease = min(change)

    #change.index(greatest_increase)+1 = month_index1
    #change.index(gretest_decrease) +1 = month_index2
    
    # Since change of date starts from the second date available, index for months is same as change index +1
    print(f"Greatest Inrease in Profits: {months[change.index(greatest_increase) +1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[change.index(greatest_decrease)+ 1]} (${greatest_decrease})")

# Write the findings to an output file
# Create path for the output file
output_file = "budget_analysis.txt"

with open(output_file, "w" ) as text:
    text.write("Financial Analysis\n")
    text.write("--------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${average_change}\n")
    text.write(f"Greatest Inrease in Profits: {months[change.index(greatest_increase) +1]} (${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {months[change.index(greatest_decrease)+ 1]} (${greatest_decrease})\n")




    




    