import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
totalMonths = 0
totalProfitLoss = 0

#Variables to calcualte change in P&L
dateList = []
profitLossChangeList = []

previousProfitLoss = 0
averageProfitLossChange = 0.0

def calculateFinancialAnalysis(budgetData, indexCounter):
    global totalMonths
    global totalProfitLoss
    global previousProfitLoss

    global dateList
    global profitLossChangeList

    profitAndLoss = int(budgetData[1])
    
     # Add each row count to the totalMonths var to add up the number of months included in the dataset
    totalMonths = totalMonths+1

    # Net total amount of P&L over the entire period
    totalProfitLoss = totalProfitLoss + profitAndLoss

    dateList.append(str(budgetData[0]))

    if(indexCounter == 0):
        previousProfitLoss = 0
        profitLossChangeList.append(0)
    else:
        profitLossChangeList.append(int(budgetData[1]) - int(previousProfitLoss))
    
    previousProfitLoss = budgetData[1]

def calculateProfitLossChangeAvg():
    global profitLossChangeList

    length = len(profitLossChangeList) - 1
    averageProfitLossChange = 0.0
    total = 0.0
    
    for profitLossChange in profitLossChangeList:
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

averageProfitLossChange = calculateProfitLossChangeAvg()  
greatestProfitLossIncrease = max(profitLossChangeList)
greatestProfitLossDecrease = min(profitLossChangeList)

totalMonthsTxt = "Total Months:" + str(totalMonths)
totalProfitLossTxt = "Total: $" + str(totalProfitLoss)
averageChangeTxt = "Average Change:" + str(round(averageProfitLossChange, 2))

# valueIndex = greatestProfitLossIncrease["ProfitLossChange"].index()
greatestIncreaseTxt = "Greatest Increase in Profits: " + str(dateList[profitLossChangeList.index(greatestProfitLossIncrease)]) + " ($" + str(greatestProfitLossIncrease) +  ")"
greatestDecreaseTxt = "Greatest Decrease in Profits:: " + str(dateList[profitLossChangeList.index(greatestProfitLossDecrease)]) + " ($" + str(greatestProfitLossDecrease)+  ")"

textFilePath = os.path.join("analysis", "analysis.txt")

fileObject = open(textFilePath, "w")
fileObject.write(headerTxt + "\n")
fileObject.write(headerTxt2 + "\n")
fileObject.write(totalMonthsTxt + "\n")
fileObject.write(totalProfitLossTxt + "\n")        
fileObject.write(averageChangeTxt + "\n")
fileObject.write(greatestIncreaseTxt + "\n")
fileObject.write(greatestDecreaseTxt + "\n")
fileObject.close()

print(headerTxt)
print(headerTxt2)
print(totalMonthsTxt)
print(totalProfitLossTxt)        
print(averageChangeTxt)
print(greatestIncreaseTxt)
print(greatestDecreaseTxt)
