#Import the necessary files
import os
import csv

#Initialize csv path to retrieve file
csvpath = os.path.join('Resources', 'election_data.csv')

#Set Variables
totalVotes = 0
CandidateList = []
CandidateDict = {}
FormattedCandidateDict = {}
electionWinner = ""

# Function to calculate the election results and add voting results to a formatted dictionary. It will also calculate the winner of the election
# Parameters:
#  None
def CalculateElectionResults():
    #setting the usage of global variables. 
    global CandidateList
    global CandidateDict
    global totalVotes
    global FormattedCandidateDict
    global electionWinner
    
    #for each candidate, add to a dictionary that will be used to calculate the number of votes for each candidate
    #frequency of candidate appearance in the list being used as an individual vote
    for candidate in CandidateList:
        if (candidate in CandidateDict):
            CandidateDict[candidate] += 1
        else:
            CandidateDict[candidate] = 1

    #Format the candidate dictionary [candidate, # of votes] to a new dictionary which will be used to print the results
    for key, value in CandidateDict.items():
        # print ("% d : % d"%(key, value))
        FormattedCandidateDict[key] = ": " + str(round(value/totalVotes*100, 4)) + "% (" + str(value) + ")"
    
    #calculate the winner based on the value (votes) of the candidate dictionary, using max function
    electionWinner = max(CandidateDict, key=CandidateDict.get)

############################################################################
######### MAIN FUNCTION ####################################################
############################################################################

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #ignore header

    #for each line, add to the total votes - calcuating this prior to calculating results, as
    #this will be used in the percentage calculation
    for row in csvreader:
        totalVotes +=1 
        CandidateList.append(row[2]) #just interested in candidates, as appearance frequency will determine votes
        
CalculateElectionResults()

#Print out the results

headerTxt = "Election Results"
lineSeperator = "-------------------------"
totalVotesTxt = "Total Votes: " + str(totalVotes)
winnerTxt = "Winner: " + str(electionWinner)

# Write data to text file
textFilePath = os.path.join("analysis", "voting_results.txt")
fileObject = open(textFilePath, "w")
fileObject.write(headerTxt + "\n")
fileObject.write(lineSeperator + "\n")
fileObject.write(totalVotesTxt + "\n")
fileObject.write(lineSeperator + "\n")        

print(headerTxt)
print(lineSeperator)
print(totalVotesTxt)
print(lineSeperator)

for key, value in FormattedCandidateDict.items():
    print(f'{key}: {value}')
    fileObject.write(f'{key}: {value}' + "\n")   

fileObject.write(lineSeperator + "\n")  
fileObject.write(winnerTxt + "\n")  
fileObject.write(lineSeperator + "\n")  
fileObject.close() 

print(lineSeperator)
print(winnerTxt)
print(lineSeperator)

