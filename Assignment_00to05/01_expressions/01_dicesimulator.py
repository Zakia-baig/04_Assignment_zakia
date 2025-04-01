# Simulate rolling two dice, three times. Prints the results of each die roll.
# This program is used to show how variable scope works.

"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their values
    """
    die1 = random.randint(1, NUM_SIDES)  # Local variable
    die2 = random.randint(1, NUM_SIDES)  # Local variable
    print(f"Die 1: {die1}, Die 2: {die2}")  # Print individual die results

def main():
    die1 = 10  # This is a different variable (in main's scope)
    print("die1 in main() starts as: " + str(die1))
    
    # Roll dice three times
    print("\nRolling dice three times:")
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("\ndie1 in main() is: " + str(die1))  # Shows main's die1 unchanged

if __name__ == "__main__":
    main()