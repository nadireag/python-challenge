# Import modules 
import os
import csv

# specify the path for the csv file
csvpath = "budget_data.csv"

# create lists to hold date, profit/loss and change info
months = []
profit_loss = []
change = []
date = []

# open the file to read
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # read the header first
    csv_header = next(csvreader)

    # append months and profit loss info to the lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # print text 
    print("Financial Analysis")
    print("--------------------------")

    # calculate the total number of months 
    total_months = len(months)
    print(f"Total Months: {total_months}")

    # loop through the list to calculate  the net total profit/losses
    total = 0
    for row in profit_loss:
        total += (row)

    # print total_profit_loss
    print(f"Total: ${total}")

    # Create change list to hold info, change list's index will be one less then profit/loss index
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

    # grab the index values
    index1 = change.index(greatest_increase)
    index2 = change.index(greatest_decrease)
    
    # for change list date starts from the second date available, index for months is same as change index +1
    print(f"Greatest Inrease in Profits: {months[(index1) +1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[(index2)+ 1]} (${greatest_decrease})")

# Create path for the output file
output_file = "budget_analysis.txt"

# write the data to the output file
output= [f"Financial Analysis\n",
             f"--------------------------\n",
             f"Total Months: {total_months}\n",
             f"Total: ${total}\n",
             f"Average Change: ${average_change}\n",
             f"Greatest Inrease in Profits: {months[index1 +1]} (${greatest_increase})\n",
             f"Greatest Decrease in Profits: {months[index2+ 1]} (${greatest_decrease})\n"]

with open(output_file, "w" ) as text: 
    text.writelines(output)
    