import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
totalMonths = 0
totalProfitLoss = 0

#Variables to calcualte change in P&L
profitLossChangeDict = {"Date": [], "ProfitLossChange": []}
previousProfitLoss = 0
averageProfitLossChange = 0.0

def calculateFinancialAnalysis(budgetData, indexCounter):
    global totalMonths
    global totalProfitLoss
    global previousProfitLoss
    global profitLossChangeDict

    profitAndLoss = int(budgetData[1])
    
     # Add each row count to the totalMonths var to add up the number of months included in the dataset
    totalMonths = totalMonths+1

    # Net total amount of P&L over the entire period
    totalProfitLoss = totalProfitLoss + profitAndLoss

    
    if(indexCounter == 0):
        previousProfitLoss = 0
        profitLossChangeDict["Date"].append(str(budgetData[0]))
        profitLossChangeDict["ProfitLossChange"].append(0)
    else:
        profitLossChangeDict["Date"].append(str(budgetData[0]))
        profitLossChangeDict["ProfitLossChange"].append(int(budgetData[1]) - int(previousProfitLoss))

    
    previousProfitLoss = budgetData[1]

def calculateProfitLossChangeAvg(profitLossChanges):
    global profitLossChangeDict 

    length = len(profitLossChangeDict["ProfitLossChange"])
    averageProfitLossChange = 0.0
    total = 0.0
    
    for profitLossChange in profitLossChanges:
            total += profitLossChange

    return total / length




#Headers to print to text file
headerTxt = "Financial Analysis"
headerTxt2 = "----------------------------"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    indexCounter = 0
    # Read each row of data after the header and send it to function for analysis calculation
    for row in csvreader:
        calculateFinancialAnalysis(row, indexCounter)
        indexCounter += 1

averageProfitLossChange = calculateProfitLossChangeAvg(profitLossChangeDict["ProfitLossChange"])  
greatestProfitLossIncrease = max(profitLossChangeDict["ProfitLossChange"])
greatestProfitLossDecrease = min(profitLossChangeDict["ProfitLossChange"])

# print(profitLossChangeDict)

totalMonthsTxt = "Total Months:" + str(totalMonths)
totalProfitLossTxt = "Total:" + str(totalProfitLoss)
averageChangeTxt = "Average Change:" + str(averageProfitLossChange)
greatestIncreaseTxt = "Greatest Increase in Profits: " + str(greatestProfitLossIncrease)
greatestDecreaseTxt = "Greatest Decrease in Profits:: " + str(greatestProfitLossDecrease)
print(headerTxt)
print(headerTxt2)
print(totalMonthsTxt)
print(totalProfitLossTxt)        
print(averageChangeTxt)
print(greatestIncreaseTxt)
print(greatestDecreaseTxt)
