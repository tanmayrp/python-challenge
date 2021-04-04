#Import the necessary files
import os
import csv
from datetime import datetime

#Lists to hold all the reformatted data
EmployeeIDList = []
FirstNameList = []
LastNameList = []
DOBList = []
SSNList = []
StateList = []

#dict for State abbreviation lookup - per special hint (thank goodness for not tying all this in ha!)
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open('employee_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #ignore header
    
    for row in csvreader:
        #Append Employee ID
        EmployeeIDList.append(row[0])

        #Split Full Name and add to First and Last Name
        fullNameSplitList = row[1].split()
        FirstNameList.append(fullNameSplitList[0])
        LastNameList.append(fullNameSplitList[1])

        #DOB Format should be MM/DD/YYYY - format and append
        dobDate = datetime.strptime(row[2], '%Y-%m-%d')
        DOBList.append(datetime.strftime(dobDate, '%m/%d/%Y'))

        #Reformat SSN to ***-**-1234 and add to list
        SSNList.append("***-**-" + row[3][-4:])

        #Reformat State to be 2 letter state abbrev
        StateList.append(us_state_abbrev[row[4]])

#Zip all lists together
cleanEmployeeDataCSV = zip(EmployeeIDList, FirstNameList, LastNameList, DOBList, SSNList, StateList)

output_file = os.path.join("clean_employee_data.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleanEmployeeDataCSV)