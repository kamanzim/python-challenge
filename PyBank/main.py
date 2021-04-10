import os
import csv

budgetdata_csv = os.path.join('.', 'Resources', 'budget_data.csv')
print("Financial Analysis")
print("----------------------------------")
with open(budgetdata_csv) as f:
    f.readline()
    total_months = 0
    total = 0
    average_change = 0
    max_profit = 0
    date_max_profit = ""
    min_profit = 0
    date_min_profit = ""
    for line in f:
        total_months = total_months + 1
        line = line.strip()
        line = line.split(",")
        date = line[0]
        date = date.split("-")
        date = date[0] + "-20" + date[1]
        profit = int(line[1])
        total = total + profit
        if total_months > 1:
            change = profit - previous_profit
            average_change = average_change + change
            if change > max_profit:
                max_profit = change 
                date_max_profit = date
            if change < min_profit:
                min_profit = change
                date_min_profit = date
        previous_profit = profit
        
        
print("total months:", total_months)
print("Total: $"+ str(total))
average_change = average_change/(total_months - 1)
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + date_max_profit + " ($" + str(max_profit) + ")")
print("Greatest Decrease in Profits: " + date_min_profit + " ($" + str(min_profit) + ")")