import random

def guess_number():
    print("=== Welcome to the Number Guessing Game! ===")
    print("Think of a number between 1 and 100")
    
    low = 1
    high = 100
    feedback = ""
    attempts = 0
    
    while feedback != "c":
        attempts += 1
        guess = random.randint(low, high)
        print(f"\nIs your number {guess}?")
        print("Enter 'c' if this is correct")
        print("Enter 'l' if your number is lower")
        print("Enter 'h' if your number is higher")
        
        feedback = input("Your response: ").lower()
        
        if feedback == "l":
            high = guess - 1
        elif feedback == "h":
            low = guess + 1
        elif feedback == "c":
            print(f"\nGreat! I guessed your number {guess} in {attempts} attempts!")
        else:
            print("Please enter a valid response (c, l, or h)")
            attempts -= 1
            
def play_again():
    return input("\nWould you like to play again? (yes/no): ").lower().startswith('y')

def main():
    print("\nLet's play a number guessing game!")
    print("I will try to guess the number you're thinking of.")
    
    while True:
        guess_number()
        if not play_again():
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()