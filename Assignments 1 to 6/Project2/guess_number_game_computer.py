import random
import time
from colorama import Fore, Style, init
import os

# Initialize colorama
init()

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    """Display welcome message and game instructions"""
    clear_screen()
    print(f"{Fore.YELLOW}{'='*60}")
    print(f"{Fore.GREEN}🎮 Welcome to the Ultimate Number Guessing Game! 🎮")
    print(f"{Fore.YELLOW}{'='*60}\n")
    print(f"{Fore.CYAN}📜 Rules of the Game:")
    print(f"{Fore.WHITE}1. Computer will choose a secret number")
    print("2. You have to guess that number")
    print("3. You'll get helpful hints after each guess")
    print("4. Try to guess in minimum attempts to get a higher score!\n")
    print(f"{Fore.GREEN}🎲 Let's begin the adventure! 🎲")
    print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
    time.sleep(2)

def get_difficulty():
    """Let player choose difficulty level"""
    while True:
        print(f"\n{Fore.CYAN}Select Your Challenge Level:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. 🌱 Easy   (1-50)   - Perfect for beginners!")
        print(f"{Fore.YELLOW}2. 🌟 Medium (1-100)  - For experienced players!")
        print(f"{Fore.RED}3. 🔥 Hard   (1-200)  - For true masters!{Style.RESET_ALL}")
        
        try:
            choice = int(input(f"\n{Fore.WHITE}Enter your choice (1-3): {Style.RESET_ALL}"))
            if choice == 1:
                return 50, "Easy"
            elif choice == 2:
                return 100, "Medium"
            elif choice == 3:
                return 200, "Hard"
            else:
                print(f"{Fore.RED}Please enter a number between 1 and 3{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter a number.{Style.RESET_ALL}")

def calculate_score(attempts, max_number):
    """Calculate player's score based on attempts and difficulty"""
    base_score = 1000
    difficulty_multiplier = max_number / 50
    return int(base_score * difficulty_multiplier / attempts)

def play_game(max_number, difficulty):
    """Main game function"""
    random_number = random.randint(1, max_number)
    attempts = 0
    guess = 0
    start_time = time.time()
    
    print(f"\n{Fore.CYAN}🎯 I'm thinking of a number between 1 and {max_number}...{Style.RESET_ALL}")
    time.sleep(1)
    
    while guess != random_number:
        try:
            guess = int(input(f"\n{Fore.WHITE}Enter your guess (1-{max_number}): {Style.RESET_ALL}"))
            attempts += 1
            
            if guess < 1 or guess > max_number:
                print(f"{Fore.RED}⚠️ Please enter a number between 1 and {max_number}{Style.RESET_ALL}")
                continue
            
            difference = abs(random_number - guess)
            if guess < random_number:
                print(f"{Fore.RED}📈 Too low!{Style.RESET_ALL}", end=" ")
                if difference > 20:
                    print(f"{Fore.YELLOW}(Hint: Try much higher!){Style.RESET_ALL}")
                elif difference > 10:
                    print(f"{Fore.YELLOW}(Hint: Try higher!){Style.RESET_ALL}")
            elif guess > random_number:
                print(f"{Fore.RED}📉 Too high!{Style.RESET_ALL}", end=" ")
                if difference > 20:
                    print(f"{Fore.YELLOW}(Hint: Try much lower!){Style.RESET_ALL}")
                elif difference > 10:
                    print(f"{Fore.YELLOW}(Hint: Try lower!){Style.RESET_ALL}")
            
        except ValueError:
            print(f"{Fore.RED}⚠️ Invalid input! Please enter a number.{Style.RESET_ALL}")
            continue
    
    # Game won
    elapsed_time = int(time.time() - start_time)
    score = calculate_score(attempts, max_number)
    
    print(f"\n{Fore.GREEN}{'🎉 ' * 5}")
    print(f"🌟 CONGRATULATIONS! 🌟")
    print(f"You've guessed the number {random_number} correctly!")
    print(f"\n📊 Game Statistics:")
    print(f"🎯 Difficulty: {difficulty}")
    print(f"🔢 Attempts: {attempts}")
    print(f"⏱️ Time: {elapsed_time} seconds")
    print(f"🏆 Score: {score} points")
    print(f"{'🎉 ' * 5}{Style.RESET_ALL}")

def play_again():
    """Ask if player wants to play again"""
    return input(f"\n{Fore.CYAN}Would you like to play again? (yes/no): {Style.RESET_ALL}").lower().startswith('y')

def main():
    """Main game loop"""
    welcome_message()
    
    while True:
        max_number, difficulty = get_difficulty()
        play_game(max_number, difficulty)
        
        if not play_again():
            print(f"\n{Fore.GREEN}Thanks for playing! See you next time! 👋{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()