import os
import csv

# path to file
file_path = os.path.join("Resources", "budget_data.csv")

#Variables
total_months = 0
net_total = 0
old_profit_loss = 0
profit_loss_changes = []
dates = []

#Budget data file
with open("Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    for row in csvreader:
        # Calculate total months
        total_months += 1
        # Calculate net total profit/loss
        net_total += int(row[1])

        # Calculate profit loss changes
        if total_months > 1:
            profit_loss_change = int(row[1]) - old_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(row[0])

        # Update old profit loss
        old_profit_loss = int(row[1])
# Calculate average change
average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)

# Find max and min profit/loss changes
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

#Print analysis results
print("Financial Analysis:")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

#Export to text file
with open("financial_analysis.txt", "w") as file:
    file.write("Financial Analysis:\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
print("Financial analysis has been exported to financial_analysis.txt.")