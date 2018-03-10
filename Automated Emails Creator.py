#Imports Modules
import csv
from itertools import zip_longest as z
import random

#A - How many lines of Data are required
#B - Imports Table creating Contents
#C - Imports Table creating Accounts
#D - Imports Table creating Region (variable Y)(csv file has no header)
#E - Imports Table creating Material (variable Z)(csv file has no header) 
#H - Creates Accounts
#J - Creates Email Content
#K - Creates Month Date
#X - Creates and Exports a Data File


#A - How many lines of Data are required

print('Make sure all data-for-table files have their headers removed' + '\n' + '' + '\n' + 'Input how many lines of data are required')
mxr = int(input())


#B - Imports Table creating Contents

with open('InputContent.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataContentTable = []
    
    for row in readCSV:
     
        column0 = row[0] # Subject
        column1 = row[1] # Weight 
        column2 = row[2] # Subject 1
        column3 = row[3] # Subject 2
        column4 = row[4] # Subject 3
        column5 = row[5] # Subject 4
        column6 = row[6] # Subject 5
        column7 = row[7] # Subject 6
        column8 = row[8] # Subject 7

        combo = [column0, column1, column2, column3, column4, column5, column6, column7, column8]

        dataContentTable = dataContentTable + [combo]


#C - Imports Table creating Accounts

with open('InputAccounts.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataAccountTable = []
    
    minValueA = 1
    
    for row in readCSV:
     
        nameAccount = row[0] # Account Name
        if nameAccount == '':
            break

        emailAccount = row[1] # Email Address 
        placeAccount = row[2] # Location
 
        weightA = int(row[3])
            
        maxValueA = minValueA + weightA - 1
      
        combo = [nameAccount, emailAccount, placeAccount, weightA, minValueA, maxValueA]
    
        dataAccountTable = dataAccountTable + [combo]
            
        minValueA = maxValueA + 1

    maxValueAccount = maxValueA # This value is used later for the random number generator


#D - Imports Table creating Region (variable Y)

with open('InputRegion.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataRegionTable = []
    
    minValueR = 1
    
    for row in readCSV:
    
        dataR = row[0]

        if dataR == '':
            break
    
        weightR = int(row[1])
            
        maxValueR = minValueR + weightR - 1
      
        combo = [dataR, weightR, minValueR, maxValueR]
    
        dataRegionTable = dataRegionTable + [combo]
            
        minValueR = maxValueR + 1

    maxValueRegion = maxValueR # This value is used when generating variable3 (Y) in the Emails


#E - Imports Table creating Material (variable Z)    
    
with open('InputMaterials.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataMaterialsTable = []
    
    minValueM = 1
    
    for row in readCSV:
    
        dataM = row[0] # Material

        if dataM == '':
            break
        
        valueM = int(row[1]) # Value
    
        weightM = int(row[2]) # Weight
            
        maxValueM = minValueM + weightM - 1
      
        combo = [dataM, valueM, weightM, minValueM, maxValueM]
    
        dataMaterialsTable = dataMaterialsTable + [combo]
            
        minValueM = maxValueM + 1

    maxValueMaterials = maxValueM # This value is used when generating variable5 (Z) in the Emails


# H - Creates Recipent and Address

mailReference = []
mailAccount = []
mailAddress = []

for counter in range (mxr):

    index = random.randint(0,maxValueAccount - 1)

    reference = counter + 1
    
    variable0 = dataAccountTable[index][0]
    variable1 = dataAccountTable[index][1]
    
    mailReference = mailReference + [reference]
    mailAccount = mailAccount + [variable0]
    mailAddress = mailAddress + [variable1]

# J - Creates Email Content

mailSubject = []
mailContent = []

for counter in range (mxr):

    index = random.randint(0,6)

    variable0 = dataContentTable[index][0] # Subject Line
    variable2 = dataContentTable[index][2]
  
    if dataContentTable[index][3] == 'X1':
        variable3 = str(format((random.randrange(1,999)* random.random() * 1000), '.2f'))
    elif dataContentTable[index][3] == 'Y':
        numberRegion = random.randint(1,maxValueRegion)
        for row in dataRegionTable:
            minValueC = int(row[2])
            maxValueC = int(row[3])
            if numberRegion >= int(row[2]) and numberRegion <= int(row[3]):
                variable3 = row[0]
    elif dataContentTable[index][3] == 'X2':
        variable3 = str(random.randint(1,99) * 100)
    else:
        variable3 = dataContentTable[index][3]
        
    variable4 = dataContentTable[index][4]
    
    if dataContentTable[index][5] == 'Z':
        numberMaterials = random.randint(1,maxValueMaterials)
        for row in dataMaterialsTable:
            if numberMaterials >= int(row[3]) and numberMaterials <= int(row[4]):
                variable5 = row[0]
                priceMat = row[1] # Used to determine the price for variable7
    else:
        variable5 = dataContentTable[index][5]
        
    variable6 = dataContentTable[index][6]
    
    if dataContentTable[index][7] == 'X3':
        variable7 = str(format(priceMat * (1 + random.random()), '.2f'))
    else:
        variable7 = dataContentTable[index][7]
    
    variable8 = dataContentTable[index][8]
    
    stringContent = variable2
    if variable3 != '#':
        stringContent = stringContent + variable3
        if variable4 != '#':
            stringContent = stringContent + variable4
            if variable5 != '#':
                stringContent = stringContent + variable5
                if variable6 != '#':
                    stringContent = stringContent + variable6
                    if variable7 != '#':
                        stringContent = stringContent + variable7
                        if variable8 != '#':
                            stringContent = stringContent + variable8
    
    mailContent = mailContent + [variable0]
    mailSubject = mailSubject + [stringContent]



    
mailDateNo = []
mailDate = []

for counter in range (mxr):
    valueD = random.randint(1, 12)

    if valueD == 1:
        date = 'Jan'
    elif valueD == 2:
        date = 'Feb'
    elif valueD == 3:
        date = 'Mar'
    elif valueD == 4:
        date = 'Apr'
    elif valueD == 5:
        date = 'May'
    elif valueD == 6:
        date = 'Jun'
    if valueD == 7:
        date = 'Jul'
    elif valueD == 8:
        date = 'Aug'
    elif valueD == 9:
        date = 'Sep'
    if valueD == 10:
        date = 'Oct'
    elif valueD == 11:
        date = 'Nov'
    elif valueD == 12:
        date = 'Dec'

    mailDate = mailDate + [date]
    mailDateNo = mailDateNo + [valueD]


#X - Creates and Exports a Data File
 
newData= [mailReference, mailAccount, mailAddress, mailContent, mailSubject, mailDate, mailDateNo]

exportData = z(*newData, fillvalue = '')

with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Discovery Emails Automated/EmailList.csv','w', newline ='') as newFile:
      writer = csv.writer(newFile)
      writer.writerows(exportData)
      newFile.close()
    
print('All Done')
    

