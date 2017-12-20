"""This function randomly chooses four colours but is giving errors when I run it..."""

import random

colours = ["Black", "White", "Green", "Yellow"]

def spin(colours):
    spin_choice = raw_input("\n\nSpin? ")
    spin_choice = spin_choice.lower()
    if spin_choice == "no":
        print "\n\nGAME OVER"
    if spin_choice == "yes":
        print "\n\n*Machine spins...*\n\n*Machine slows...*\n\n*Machine stops*\n\n"
        slot_1 = (random.choice(colours))
        slot_2 = (random.choice(colours))
        slot_3 = (random.choice(colours))
        slot_4 = (random.choice(colours))
        print "Slot One: " + slot_1 + "   " + "Slot Two: " + slot_2 + "   " + "Slot Three: " + slot_3 + "   " + "Slot Four: " + slot_4
    else:
        "Input invalid, please enter either 'yes' or 'no'"

spin(colours)
