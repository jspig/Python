import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
    """ Initiates guessing game with flesh organism """
    def __init__(self):
        """Sets everything up to work how I program it"""
        EasyFrame. __init__(self, title = "Guessing Game")
        #Set Variable
        self.myNumber = random.randint(1, 100)
        self.count = 0
        greeting = "Guess a number between 1 and 100."
        self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0,
                                       sticky = "NSEW",
                                       columnspan = 2)
        self.addLabel(text = "Your Guess", row = 1, column = 0)
        self.guessField = self.addIntegerField(0, row = 1, column =1)
        self.nextButton = self.addButton (text = "Next", row = 2, column = 0)
        self.newButton = self.addButton (text = "New game", row = 2, column =1)

def main():
        """Abra-ka-Dabra the window appears"""
        GuessingGame().mainloop()
if __name__ == "__main__":
    main()

def nextGuess(self):
    """Obvious Fleshling"""
    self.count += 1
    guess = self.guessField.getNumber()
    if guess == self.myNumber:
        self.hintLabel["text"] = "You've guessed it in " + \
                                 str(self.count) + "attempts!"
        self.nextButton["state"] = "disabled"
    elif guess < self.myNumber:
        self.hintLabel["text"] = "Sorry, too small! "
    else:
        self.hintLabel["text"] = "Sorry, too large!"
def newGame(self):
    """Reset Noob"""
    self.myNumber = random.randint(1,100)
    self.count = 0
    greeting = "Guess a number between 1 and 100."
    self.hintLabel ["text"] = greeting
    self.guessField.setNumber(0)
    self.nextButton["state"] = "Normal"
