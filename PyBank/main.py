#Import the necessary files
import os
import csv

#Initialize csv path to retrieve file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Variables to calculate total months and net total PnL
totalMonths = 0
totalProfitLoss = 0

#Variables to calcualte change in PnL
dateList = []
profitLossChangeList = []
previousProfitLoss = 0
averageProfitLossChange = 0.0

# Function to calculate the Financial Analysis for Total Months, Net Total PnL, and keep running list of PnL Change
# Parameters:
#   budgetData - row of data rom the budget_data.csv; includes Date and PnL
#   indexCounter - conuter to measure if this is the first row of data. 
def calculateFinancialAnalysis(budgetData, indexCounter):

    #defining global vars here. 
    global totalMonths
    global totalProfitLoss
    global previousProfitLoss
    global dateList
    global profitLossChangeList

    # Add each row count to the totalMonths var to add up the number of months included in the dataset
    totalMonths += 1
    
    
    #set PnL var
    profitAndLoss = int(budgetData[1])

    # Net total amount of P&L over the entire period
    totalProfitLoss += profitAndLoss


    #dateList used to manage dates to be utilized for Min/Max print outs
    dateList.append(str(budgetData[0]))

    #If its the first row of the CSV, set PnL change to - and append that 0 to the PnLChangeList
    #PnLChangeList to be used for Avg change Pnl and Min/Max print outs
    if(indexCounter == 0):
        previousProfitLoss = 0
        profitLossChangeList.append(0)
    else:
        profitLossChangeList.append(int(budgetData[1]) - int(previousProfitLoss))
    
    previousProfitLoss = budgetData[1]

#Function to calculate the PnL Change Average
def calculateProfitLossChangeAvg():
    global profitLossChangeList

    length = len(profitLossChangeList) - 1
    averageProfitLossChange = 0.0
    total = 0.0
    
    for profitLossChange in profitLossChangeList:
            total += profitLossChange

    return total / length

############################################################################
######### MAIN FUNCTION ####################################################
############################################################################

#CSV Management
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #ignore header
    indexCounter = 0

    # Calculate Financial Analysis for each row
    for row in csvreader:
        calculateFinancialAnalysis(row, indexCounter)
        indexCounter += 1

#Calculate Avg PNL change, and Min/Max values
averageProfitLossChange = calculateProfitLossChangeAvg()  
greatestProfitLossIncrease = max(profitLossChangeList)
greatestProfitLossDecrease = min(profitLossChangeList)

#Set string vars to be used to print to text and terminal
headerTxt = "Financial Analysis"
headerTxt2 = "----------------------------"
totalMonthsTxt = "Total Months: " + str(totalMonths)
totalProfitLossTxt = "Total: $" + str(totalProfitLoss)
averageChangeTxt = "Average Change:" + str(round(averageProfitLossChange, 2))
greatestIncreaseTxt = "Greatest Increase in Profits: " + str(dateList[profitLossChangeList.index(greatestProfitLossIncrease)]) + " ($" + str(greatestProfitLossIncrease) +  ")"
greatestDecreaseTxt = "Greatest Decrease in Profits:: " + str(dateList[profitLossChangeList.index(greatestProfitLossDecrease)]) + " ($" + str(greatestProfitLossDecrease)+  ")"

# Write data to text file
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

#Write data to terminal
print(headerTxt)
print(headerTxt2)
print(totalMonthsTxt)
print(totalProfitLossTxt)        
print(averageChangeTxt)
print(greatestIncreaseTxt)
print(greatestDecreaseTxt)

##########################################################################################################