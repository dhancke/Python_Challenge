# File path associated with the file across OS
import os

# Module for reading CSV files:
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    print(csvreader)

# Read header row first:
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Parameters forthe variables below:
    
    total_months = 0
    total_profit_or_loss = 0
    daily_change = 0
    previous_value = 0
    total_change = 0
    change_count = 0
    greatest_increase = 0
    greatest_decrease = 0 

# Read each row of data after header: Loop  
    for row in csvreader:
        
#Calculate the total number of months in the dataset
        total_months = (total_months + 1)
      
#Calculate the total amount of "Profit/Losses"over the entire period
        total_profit_or_loss += int(row[1])


#Give the change in "Profit/Losses" over the entire period, and the average
        if total_months == 1:
            daily_change = int(row[1]) - int(row[1])
            previous_value = int(row[1])
        else: 
            daily_change = int(row[1]) - previous_value
            previous_value = int(row[1])
            change_count += 1

            total_change += daily_change
     

#Greatest increase in profits (date & amount) over the entire period
        if daily_change >= greatest_increase:
            greatest_increase = daily_change
            greatest_increase_date = (row[0])

#Greatest decrease in profits (date & amount) over the entire period
        if daily_change <= greatest_decrease:
            greatest_decrease = daily_change
            greatest_decrease_date = (row[0])


#Print the analysis and export a text file with results
    average_changes = total_change / change_count

    print(f"Total months: {total_months}") 
    print(f"Total profit / loss: ${total_profit_or_loss}")
    print(f"Average changes: ${average_changes}") 
    print(f"Greatest increase in profits: {greatest_increase_date} (${greatest_increase})")  
    print(f"Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})")  

# Module for writing output files:
outputpath = os.path.join('Analysis', 'output.txt')
with open(outputpath, 'w') as file:
    file.writelines("Financial Analysis\n")
    file.writelines("------------------\n")
    file.writelines("Total months: " + str(total_months) + "\n")
    file.writelines("Total profit / loss: $" + str(total_profit_or_loss) + "\n")
    file.writelines("Average changes: $" + str(average_changes) + "\n")
    file.writelines("Greatest increase in profits: " + str(greatest_increase_date) + "($"+str(greatest_increase) + ")\n")
    file.writelines("Greatest decrease in profits: " + str(greatest_decrease_date) + "($"+str(greatest_decrease) + ")\n")