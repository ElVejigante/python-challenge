#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#* The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" (pnl) over the entire period
#  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

month_list = []
pnl_change_list = []
month_count = 0
net_pnl = 0
previous_month_pnl = 0
current_month_pnl = 0
pnl_change = 0

# CSV file path
budget_data_path = os.path.join("Resources", "budget_data.csv")
# read and write in various formats
with open(budget_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#stores header row
    csv_header = next(csvfile)
    for row in csv_reader:
#for total months
        month_count = month_count + 1
        current_month_pnl = int(row[1])
#Net Profit/Losses
        net_pnl = net_pnl + current_month_pnl
        if (month_count == 1):
            previous_month_pnl = current_month_pnl
        else:
#Profit/Loss changes
            pnl_change = current_month_pnl - previous_month_pnl
            month_list.append(row[0])
            pnl_change_list.append(pnl_change)
            previous_month_pnl = current_month_pnl
    sum_pnl = sum(pnl_change_list)
#Average Profit/Losses
    average_pnl = round(sum_pnl/(month_count - 1), 2)
#Greatest Increases/Decreases of Profits/Losses
    highest_change = max(pnl_change_list)
    lowest_change = min(pnl_change_list)
    highest_index = pnl_change_list.index(highest_change)
    lowest_index = pnl_change_list.index(lowest_change)
    best_month = month_list[highest_index]
    worst_month = month_list[lowest_index]
#Print to terminal, export to txt file
results = (f"Financial Analysis\n----------------------------\nTotal Months:  {month_count}\nTotal:  ${net_pnl}\nAverage Change:  ${average_pnl}\nGreatest Increase in Profits:  {best_month} (${highest_change}\nGreatest Decrease in Losses:  {worst_month} (${lowest_change})") 
print(results)
pyBank_txt = os.path.join("Results", "pyBank_Analysis.txt")
with open(pyBank_txt, "w") as text:
    text.write(results)
