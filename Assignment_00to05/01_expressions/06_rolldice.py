# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def roll_dice():
    """Simulates rolling two dice and prints the results"""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total: {total}\n")

print("Dice Rolling Simulator")
print("----------------------")
roll_dice()