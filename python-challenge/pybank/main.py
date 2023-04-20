
# PyBank Challenge

#import library
import csv
import os

# create path to input the file
csvpath = os.path.join('Resources', 'budget_data_resource.csv')


# Create lists for the dataset
profit_loss_list = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# open the csv file and rename it then read it using a with loop
with open(csvpath) as pybank_file:
    csvreader = csv.reader(pybank_file, delimiter=',')

    # Set up the header rows to the correct position
    header = next(csvreader)
    first_row = next(csvreader)  # this value is equal to jan-10, 1088983

    # Setting information for the first row
    total_months = 1
    total_net = int(first_row[1])
    previous_net = int(first_row[1])  # this value is equal to jan-10, 1088983

    for row in csvreader:
        # Find the total number of months
        # this line of code is starting from a variable of 1 and adding to it
        total_months = total_months+1

        # Add the data from profit/losses column to the list
        profit_loss_list.append(int(row[1]))

        # Find the monthly changes
        # int(row[1]) is starting at feb-10th's data while prev_net is
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        # add that data into the net change list
        net_change_list.append(net_change)

        # Find the greatest increase in profits
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Find the greatest decrease in profits
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    # Financial analysis of the data
    print("Financial Analysis:")

    # Total number of months included in the dataset
    print(f"Total months = {total_months}")

    # Net total amount of profit/losses
    # add in the first row of data (jan-10) so it is included in the sum
    profit_loss_list.append(int(first_row[1]))
    total_net = sum(profit_loss_list)
    print(f"The total net amount of profits/losses is {total_net}")

    # Find the average of the changes in profit/losses
    avg_changes = sum(net_change_list) / len(net_change_list)
    print(f"The average changes in profits/losses is {avg_changes}")

    # Print the greatest increase/decrease results
    print(
        f"The greatest increase in profits was on {greatest_increase[0]} with a total increase of ${greatest_increase[1]}")
    print(
        f"The greatest decrease in profits was on {greatest_decrease[0]} with a total decrease of ${greatest_decrease[1]}")

#create a text file that has the results from the analysis   
analysis_path = os.path.join('Analysis', 'budget_analysis_txt')   
with open(analysis_path, 'w') as txt_file:
     output=(
         f"Financial Analysis:\n"
         f"Total months = {total_months}\n"
         f"The total net amount of profits/losses is {total_net}\n"
         f"The average changes in profits/losses is {avg_changes}\n"
         f"The greatest increase in profits was on {greatest_increase[0]} with a total increase of ${greatest_increase[1]}\n"
         f"The greatest decrease in profits was on {greatest_decrease[0]} with a total decrease of ${greatest_decrease[1]}\n"
         )
     
     print(output)
     txt_file.write(output)