game = input("Enter name of game = ")
buyIn = input("Enter buyIn = ")
pot = input("Enter pot amount = ")
winningRoll = input("Enter the winning roll: ")
import random
for roll in range (1):
    print(random.randint(1,6) + random.randint(1,6), end = "  ")
if roll !=7:
    print("You Lose.")
else:
    print("You Win.")
    
    
    


        

    
