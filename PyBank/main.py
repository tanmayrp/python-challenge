import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
totalMonths = 0
totalProfitLoss = 0


def calculateFinancialAnalysis(budgetData):
    global totalMonths
    global totalProfitLoss

    profitAndLoss = int(budgetData[1])
    
     # Add each row count to the totalMonths var to add up the number of months included in the dataset
    totalMonths = totalMonths+1

    # Net total amount of P&L over the entire period
    totalProfitLoss = totalProfitLoss + profitAndLoss




#Headers to print to text file
headerTxt = "Financial Analysis"
headerTxt2 = "----------------------------"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Read each row of data after the header and send it to function for analysis calculation
    for row in csvreader:
        calculateFinancialAnalysis(row)

        


totalMonthsTxt = "Total Months:" + str(totalMonths)
totalProfitLossTxt = "Total:" + str(totalProfitLoss)
print(headerTxt)
print(headerTxt2)
print(totalMonthsTxt)
print(totalProfitLossTxt)        