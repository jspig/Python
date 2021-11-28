"""
File: average.py
Project 6.9
Prints the average of the numbers in a text file 
"""

from functools import reduce
import math

# Accept the input file name and open the file
fileName = input("Enter the input file name: ")
inputFile = open(fileName, 'r')

# Read the numbers as strings into a list
lyst = []
for line in inputFile:
    lyst.extend(line.split())

# Convert all the strings in the list to numbers
lyst = list(map(float, lyst))

# Compute the sum of the numbers
summation = reduce(lambda x, y: x + y, lyst)

# Print the average
if len(lyst) == 0:
    average = 0
else:
    average= summation / len(lyst)
print("The average is", average)

##To print the minimum/maximum of the numbers
"""I used recursive functions"""

if len(lyst) !=0:
    print("The minmum number is", min(lyst))
else:
    print("The maximum number is", max(lyst))

if len(lyst) !=0:
    print("The maximum number is", max(lyst))
else:
    print("The minimum number is", min(lyst))

