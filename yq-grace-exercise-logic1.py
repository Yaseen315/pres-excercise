"""This is my random number generator, I have a few problems with it. The turns don't seem to be working properly- I want them to start from 1
and increase each turn. Also the print statements seem to not be coming out the way I want them. I also can't make the game finish."""

print "Random number generator"

from random import randint

answer = randint(1, 101)
turn = 0

while turn < 5:
    print "Turn", turn
    user_guess = int(raw_input("Guess a number between 1 and 100:"))

    if user_guess == answer:
        print "You got it right!"
        print "You got my number in" + str(turn) + "turns"
    else:
        if user_guess < 1 or user_guess > 100:
            print "Not in range"
            turn += 1
        elif user_guess > answer:
            print "Too high"
            turn += 1
        elif user_guess < answer:
            print "Too low"
            turn += 1
        
if turn == 5:
    print "Game Over."