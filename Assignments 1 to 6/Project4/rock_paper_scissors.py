import random
import time

def get_user_choice():
    while True:
        choice = input("\nEnter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if choice in ['rock', 'paper', 'scissors', 'q']:
            return choice
        print("Invalid choice! Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Dictionary defining what each choice beats
    wins_against = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if user_choice == computer_choice:
        return 'tie'
    elif wins_against[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

def display_choices(user_choice, computer_choice):
    print("\nRock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def play_game():
    print("\n=== Welcome to Rock, Paper, Scissors! ===")
    print("First to win 3 rounds is the champion!")
    
    user_score = 0
    computer_score = 0
    rounds_played = 0
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'q':
            break
            
        computer_choice = get_computer_choice()
        rounds_played += 1
        
        display_choices(user_choice, computer_choice)
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            user_score += 1
            print("\n🎉 You win this round! 🎉")
        elif winner == 'computer':
            computer_score += 1
            print("\n💻 Computer wins this round! 💻")
        else:
            print("\n🤝 It's a tie! 🤝")
            
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        # Check if someone has won 3 rounds
        if user_score == 3 or computer_score == 3:
            print("\n=== Game Over ===")
            print(f"Total rounds played: {rounds_played}")
            if user_score > computer_score:
                print("🏆 Congratulations! You are the champion! 🏆")
            else:
                print("🤖 Computer is the champion! Better luck next time! 🤖")
            break

def main():
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if not play_again.startswith('y'):
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()