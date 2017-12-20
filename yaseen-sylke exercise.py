# Imports random module
import random 
# This generates a random number from 0 to 99 including.
randomNumber= random.randrange(0, 100)
print "The random number has been  generated"

guessed = False


while guessed == False: 
    # turns userinput into an integer
    userInput = int(input("Take your guess!"))
    if userInput == randomNumber:
        # Breaks while loop
        guessed = True
        # Ensures valid guesses
        print "Well Done!"
    elif userInput > 100:
        print "Below 100 please"
    elif userInput < 0:
        print "Bit higher!"
        # Direct user to correct number
    elif userInput > randomNumber:
        print "Try again!"
    elif userInput < randomNumber:
        print "try guessing higher"
    
    import time

print "Game over!"
    