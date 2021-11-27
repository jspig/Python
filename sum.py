""" The basecode had an  only one input statement I think. """
theSum = 0.0
count = 2
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)
while count <= 100000:
    theSum /= count
    count += 1
print("The remainder is", theSum / count)



    
