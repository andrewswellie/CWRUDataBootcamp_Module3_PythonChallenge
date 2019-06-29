### PyBank
#
#![Revenue](Images/revenue-per-lead.jpg)
#
#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#
#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#
#  * The total number of months included in the dataset
#
#  * The net total amount of "Profit/Losses" over the entire period
#
#  * The average of the changes in "Profit/Losses" over the entire period
#
#  * The greatest increase in profits (date and amount) over the entire period
#
#  * The greatest decrease in losses (date and amount) over the entire period
#
#* As an example, your analysis should look similar to the one below:
#
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```
#
##* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#

# Imports the OS and CSV modules necessary to complete the exercise
import os
import csv

# Establishes date,revenue, revenue change, and report (for output) variables as lists so I can append them later with a for loop
date = []
revenue = []
revenue_change = []
report = []

#Opens the directory that contains the csv file, sets the delimiter as ",", and establishes the variable csvfile as the data file
resource_csv = os.path.join('budget_data.csv')
with open(resource_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvfile = csv.reader(csvfile)
    csv_header = next(csvreader)
        
# For loop that will add all the instances of a date and revenue to their list variables. Made sure to cast both to their appropriate variable type. Making sure to indent within the opened CSV file
    for row in csvfile:
       date.append(str(row[0]))
       revenue.append(int(row[1])) 

# calculating the total months using len and the total revenue using a sum   
    ttl_months = len(revenue)
    total_revenue = sum(revenue)
    
# For Loop that calculates the avg revenue change, greatest increase, and greatest decrease, and stores them to their own variables
    for i in range(len(revenue)-1):
        revenue_change.append(revenue[i+1]-revenue[i])
    average_revenue_change = sum(revenue_change)/len(revenue_change)
    max_revenue_change = max(revenue_change)
    min_revenue_change = min(revenue_change)

# Appends my report list with the strings of text that include the outputs of my financial calculations. Makes sure to break the information into their own new lines    
    report.append('Financial Analysis''\n')
    report.append('--------------------------------------------------'+'\n')
    report.append('Total Months: '+str(ttl_months)+'\n')
    report.append('Total: $'+str(total_revenue)+'\n')
    report.append('Average Change: $'+str(average_revenue_change)+'\n')
    report.append('Greatest Increase in Profits: '+str(date[revenue_change.index(max_revenue_change)+1])+' ($'+str(max_revenue_change)+')'+'\n')
    report.append('Greatest Decrease in Profits: '+str(date[revenue_change.index(min_revenue_change)+1])+' ($'+str(min_revenue_change)+')\n')

# Prints my report list to the console as well as creating a new .txt file called output_budget.txt that includes the same information
    for line in report:
        print(line,end='')
    with open('output_budget.txt','w') as output:
        output.writelines(report)