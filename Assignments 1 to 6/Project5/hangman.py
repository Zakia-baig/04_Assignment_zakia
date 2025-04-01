import random

# Dictionary of fruits with their characteristics
fruits = {
    "apple": {
        "color": "red or green",
        "taste": "sweet and crisp",
        "shape": "round",
        "hint1": "Keeps the doctor away",
        "hint2": "Snow White ate this"
    },
    "banana": {
        "color": "yellow",
        "taste": "sweet and soft",
        "shape": "curved",
        "hint1": "Monkeys love it",
        "hint2": "Comes in bunches"
    },
    "orange": {
        "color": "orange",
        "taste": "citrusy and sweet",
        "shape": "round",
        "hint1": "Named after its color",
        "hint2": "Rich in Vitamin C"
    },
    "strawberry": {
        "color": "red",
        "taste": "sweet and tangy",
        "shape": "heart-shaped",
        "hint1": "Often dipped in chocolate",
        "hint2": "Seeds on the outside"
    },
    "mango": {
        "color": "yellow and orange",
        "taste": "sweet and juicy",
        "shape": "oval",
        "hint1": "King of fruits",
        "hint2": "Popular in tropical countries"
    }
}

def play_game():
    print("\n=== Fruit Guessing Game ===")
    print("Guess the fruit based on its characteristics!")
    
    # Select random fruit
    fruit_name = random.choice(list(fruits.keys()))
    fruit_info = fruits[fruit_name]
    attempts = 0
    hints_given = 0
    
    # List to store used hints
    used_characteristics = []
    
    while True:
        if attempts == 0:
            print("\nI'm thinking of a fruit...")
        
        # Display menu
        print("\nWhat would you like to know about the fruit?")
        options = ["Color", "Taste", "Shape", "Get a hint", "Make a guess"]
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            attempts += 1
            
            if choice == 1:
                if "color" not in used_characteristics:
                    print(f"\nThe fruit is {fruit_info['color']}")
                    used_characteristics.append("color")
                else:
                    print("\nYou already know the color!")
                    attempts -= 1
                    
            elif choice == 2:
                if "taste" not in used_characteristics:
                    print(f"\nThe fruit tastes {fruit_info['taste']}")
                    used_characteristics.append("taste")
                else:
                    print("\nYou already know the taste!")
                    attempts -= 1
                    
            elif choice == 3:
                if "shape" not in used_characteristics:
                    print(f"\nThe fruit is {fruit_info['shape']}")
                    used_characteristics.append("shape")
                else:
                    print("\nYou already know the shape!")
                    attempts -= 1
                    
            elif choice == 4:
                if hints_given == 0:
                    print(f"\nHint: {fruit_info['hint1']}")
                    hints_given += 1
                elif hints_given == 1:
                    print(f"\nHint: {fruit_info['hint2']}")
                    hints_given += 1
                else:
                    print("\nNo more hints available!")
                    attempts -= 1
                    
            elif choice == 5:
                guess = input("\nWhat fruit do you think it is? ").lower()
                if guess == fruit_name:
                    print(f"\nCongratulations! 🎉")
                    print(f"You guessed it in {attempts} attempts!")
                    return True
                else:
                    print("\nSorry, that's not correct. Try getting more information!")
                    
            else:
                print("\nPlease enter a number between 1 and 5!")
                attempts -= 1
                
        except ValueError:
            print("\nPlease enter a valid number!")
            attempts -= 1

# Start the game
while True:
    play_game()
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() not in ['y', 'yes']:
        print("\nThanks for playing! Goodbye! 🍎🍌🍊")
        break