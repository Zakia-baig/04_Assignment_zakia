"""Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48"""

import random

def guess_my_number():
    print("Guess My Number")
    print("I am thinking of a number between 0 and 99...")
    
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    guess = None
    attempts = 0
    
    while guess != secret_number:
        try:
            guess = int(input("Enter a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                print(f"You found it in {attempts} attempts!")
                
        except ValueError:
            print("Please enter a valid number between 0 and 99.")

# Start the game
guess_my_number()
