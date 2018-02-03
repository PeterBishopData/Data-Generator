#Imports Modules
import csv
from itertools import zip_longest as z
import random

#A - Opens File and Imports Table creating Lists
#B - Creates Data List
#X - Creates and Exports a Data File


#A - Opens File and Imports Table creating Lists

#Number Data Sets

print ("Input the number of data sets required")

noDSet = int(input())

#A1 - Data Set Account Details

with open('Index List.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')
    dataListA1 = []
    
    minValue = 1
    
    for row in readCSV:
    
        account = row[0]

        if account == '':

            break
        
        address = row[1]
    
        weight = int(row[2])
            
        maxValue = minValue + weight - 1
      
        combo = [account, address, minValue, maxValue]
    
        dataListA1 = dataListA1 + [combo]
            
        minValue = maxValue + 1

    maxValueA1 = maxValue
    
#A2 - Data Set 2

with open('Index List.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataListA2 = []
    
    minValue = 1
    
    for row in readCSV:
    
        data = row[2]

        if data == '':

            break
    
        weight = int(row[3])
            
        maxValue = minValue + weight - 1
      
        combo = [data, weight, minValue, maxValue]
    
        dataListA2 = dataListA2 + [combo]
            
        minValue = maxValue + 1

    maxValueA2 = maxValue


#B - Creates Data List

#B1  - Data Set 1

outputDataListA1 = [['Reference', 'Account', 'Email Address']]

for counter in range (0,noDSet):

    index = random.randint(1,maxValueA1)
    
    reference = counter + 1
    
    combo = []
    
    for row in dataListA1:
        
        minValueC = int(row[3])
        maxValueC = int(row[4])
       
        if index >= int(row[3]) and index <= int(row[4]):
            
            combo =[reference, row[0], row[1]]
            
            outputDataListA1 = outputDataListA1 + [combo]
                  
#B2  - Data Set 2

outputDataListA2 = [['County']]

for counter in range (0,noDSet):

    index = random.randint(1,maxValueA2)
    
    for row in dataListA2:
        
        minValueC = int(row[2])
        maxValueC = int(row[3])
       
        if index >= int(row[2]) and index <= int(row[3]):
            
            outputDataListA2 = outputDataListA2 + [[row[0]]]

              
#X - Creates and Exports a Data File

exportReference = []
exportType = []
exportCounty = []

for mark in range (0, noDSet):

    exportReference = exportReference + [outputDataListA1[mark][0]]
    exportType = exportType + [outputDataListA1[mark][1]]
    exportCounty = exportCounty + [outputDataListA2[mark][0]]
    
newData = [exportReference, exportType, exportCounty]

exportData = z(*newData, fillvalue = '')  

with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Data Generator/Output.csv','w', newline ='') as newFile:
      writer = csv.writer(newFile)
      writer.writerows(exportData)
      newFile.close()
    
print('All Done')
    
