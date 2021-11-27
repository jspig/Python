"""
Program: payroll.py
Project 4.12

Print a payroll report.

Input
   A file in which each line has the form
   
   <last name/employeeID/address> <hourly wage> <hours worked> 

Output
   A report in tabular format.  Each line has the form

   <last name/employeeID/address> <hours worked> <total wages> 
   
"""
 

# Take the inputs
fileName = input("Enter the file name: ")

# Open the input file
inputFile = open(fileName, 'r')

# Read the data and print the report
print("%-15s%6s%15s" % ("Name/ID/Add", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split ()
    name = dataList[0]
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours * payRate
    print("%-15s%6d%15.2f" % (name, hours, totalPay))

    
